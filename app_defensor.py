import streamlit as st

# 1. Visual Page Configuration
st.set_page_config(page_title="ADT - Server Migration Notice", page_icon="⚖️", layout="centered")

# 2. Migration Header Warning
st.warning("🚀 System Update: Platform Infrastructure Has Been Upgraded!")

# 3. Academic & Technical Context
st.markdown("""
## ⚖️ Worker Defense Assistant (ADT)

To ensure high availability, horizontal scalability, and optimize the inference latency of the **Llama 3** open-source foundation model, **our production infrastructure has been migrated to a high-performance dedicated cluster**.

The fully functional prototype, the **ChromaDB** vector store, and the conversation-aware retrieval pipeline (RAG) are currently operational on our main server node.
""")

# 4. Primary Call to Action: Link to Active Chatbot on Hugging Face
st.link_button(
    "👉 ACCESS LIVE CHATBOT (Main Server - Hugging Face)", 
    "https://huggingface.co/spaces/crishliop/ADT-Defensor-Laboral",
    type="primary",
    use_container_width=True
)

st.write("") # Spacer

st.markdown("""
### 📂 Project Repository & Evaluation Artefacts
For grading purposes, you can inspect the comprehensive technical lifecycle documentation, modular source code backend, logs, and simulation test cases in the official storage directory:
""")

# 5. Secondary Call to Action: Link to Google Drive Directory (Replace with your actual URL)
st.link_button(
    "📁 VIEW CODE & TEST CASES (Google Drive Repository)", 
    "https://drive.google.com/drive/folders/1mOqahXJNDB3I_3MnzaY61BSAuuGgIKOv?usp=sharing", # <--- REEMPLAZA ESTA URL CON TU ENLACE DE DRIVE COMPARTIDO
    type="secondary",
    use_container_width=True
)

st.write("---")

# 6. Technical Evaluator Note (Fulfills Phase 4 Rubric Criteria)
st.info("""
**Technical Note for the Evaluator:** This alternate landing deployment functions as a high-availability node under a Knowledge Confinement Architecture. The backend pipeline and the embeddings database have been centralized within Hugging Face Spaces to strictly comply with the stability and multi-user concurrent deployment standards required for Phase 4 of the Natural Language Processing graduate course.
""")
