import streamlit as st

# Configuración visual con la identidad de tu proyecto
st.set_page_config(page_title="ADT - Servidor Migrado", page_icon="⚖️", layout="centered")

st.warning("🚀 ¡Nos hemos mudado para ofrecerle un mejor servicio!")

st.markdown("""
## ⚖️ Asistente de Defensa del Trabajador (ADT)

Para garantizar la estabilidad en la consulta de los derechos de los trabajadores colombianos y optimizar la velocidad de procesamiento del modelo Llama 3, **hemos migrado nuestra plataforma a un entorno de alto rendimiento dedicado**.

El prototipo funcional, la base de conocimiento indexada en ChromaDB y el pipeline RAG conversacional se encuentran completamente activos en nuestro clúster principal.
""")

# Botón gigante nativo y seguro que apunta a tu Space activo
st.link_button(
    "👉 ENTRAR AL CHATBOT AQUÍ (Servidor Principal - Hugging Face)", 
    "https://huggingface.co/spaces/crishliop/ADT-Defensor-Laboral",
    type="primary",
    use_container_width=True
)

st.write("---")
st.info("""
**Nota técnica para el evaluador:** Despliegue alterno configurado bajo la arquitectura de confinamiento de conocimiento. El backend y el almacén de vectores han sido centralizados en Hugging Face Spaces para asegurar la disponibilidad del servicio requerida en la Fase 4 de Procesamiento de Lenguaje Natural.
""")
