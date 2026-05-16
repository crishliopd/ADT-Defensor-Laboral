import sys

# 1. Parche para la base de datos (Evita errores de versión de SQLite)
try:
    __import__('pysqlite3')
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError:
    pass

# 2. Parche para el error de Protobuf (El que te está saliendo ahora)
import os
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. Configuración General
load_dotenv()
st.set_page_config(page_title="ADT - Defensor Laboral", page_icon="⚖️")
st.title("⚖️ Asistente de Defensa del Trabajador (ADT)")

# 2. Inicialización del Sistema RAG (Mejorado para buscar más contexto)
@st.cache_resource
def configurar_motor_rag():
    # Embeddings multilingües
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    
    # Carga de documentos con codificación UTF-8
    loader = DirectoryLoader(
        './documentos_legales/', 
        glob="./*.txt", 
        loader_cls=TextLoader,
        loader_kwargs={'encoding': 'utf-8'}
    )
    docs = loader.load()
    
    # Fragmentación estratégica (Chunking)
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    
    # Base de datos vectorial persistente (ChromaDB)
    vectorstore = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory="./chroma_db"
    )
    
    # MEJORA: Aumentamos 'k' a 5 para que lea más leyes antes de responder
    return vectorstore.as_retriever(search_kwargs={"k": 5})

# 3. Lógica del Modelo de Lenguaje (LLM)
retriever = configurar_motor_rag()

api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile", 
    temperature=0.3, 
    groq_api_key=api_key
)
# 4. Prompt de Sistema "Experto"
template = """Actúa como el 'Defensor Laboral ADT', un experto en derecho laboral colombiano. 

Tu misión es asesorar al trabajador usando los documentos proporcionados. Sigue estas reglas:
1. SIEMPRE cita el artículo del Código Sustantivo del Trabajo o la Ley 2466 de 2025.
2. Si existen sentencias en el contexto, úsalas para reforzar el argumento.
3. Prioriza explicar el 'Debido Proceso' en casos de despido o sanciones.
4. Mantén un tono profesional, empático y protector del trabajador.

Estructura:
- 🛡️ **Análisis de tu caso:** (Resumen).
- ⚖️ **Soporte Legal:** (Artículos y leyes específicos).
- 👨‍🏫 **Recomendación ADT:** (Pasos prácticos a seguir).

Contexto Legal:
{context}

Pregunta del Trabajador: {question}

Respuesta del Defensor ADT:"""

prompt = ChatPromptTemplate.from_template(template)

# Cadena RAG con estándar LCEL (2026)
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 5. Interfaz de Usuario (Historial de Chat)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("¿Qué duda tienes sobre tu trabajo hoy?"):
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    with st.chat_message("assistant"):
        with st.spinner("Buscando en leyes y sentencias..."):
            respuesta = rag_chain.invoke(user_input)
            st.markdown(respuesta)
            st.session_state.chat_history.append({"role": "assistant", "content": respuesta})
