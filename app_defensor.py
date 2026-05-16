import streamlit as st

# Configuración básica de la página para que no se vea vacía mientras redirige
st.set_page_config(page_title="ADT - Redireccionando", page_icon="⚖️")

# Tu URL oficial y activa en Hugging Face Spaces
url_hugging_face = "https://huggingface.co/spaces/crishliop/ADT-Defensor-Laboral" 

st.markdown(f"""
    <div style="text-align: center; margin-top: 50px;">
        <h2>⚖️ Asistente de Defensa del Trabajador (ADT)</h2>
        <p>Estamos optimizando la infraestructura para mejorar la velocidad del servicio.</p>
        <p><b>Redireccionando automáticamente a nuestro servidor principal...</b></p>
        <p>Si no redirige en unos segundos, <a href="{url_hugging_face}" target="_top">haga clic aquí</a>.</p>
    </div>
    
    <script>
        // Este script rompe el iframe de Streamlit y redirige la pestaña completa
        window.top.location.href = "{url_hugging_face}";
    </script>
""", unsafe_warning=False, unsafe_allow_html=True)
