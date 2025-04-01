# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 12:15:26 2025

@author: jperezr
"""

import streamlit as st
import base64

# Configuración de la página
st.set_page_config(
    page_title="RAP PENSIONISSSTE",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar con información del autor
with st.sidebar:
    st.title("Créditos")
    st.markdown("---")
    st.subheader("Autor de la letra")
    st.markdown("""
    **Javier Horacio Pérez Ricárdez**  
    *Analista UEAP "B"*  
    *Subdirección de Planeación Estratégica*
    """)
    st.markdown("---")
    #st.image("https://cdn.pixabay.com/photo/2017/01/31/15/33/avatar-2027360_640.png", 
    #         width=150, caption="Autor del RAP")

# Función para mostrar audio con estilo
def styled_audio_player(audio_file, title, color):
    try:
        audio_bytes = open(audio_file, "rb").read()
        st.markdown(f"""
        <div style="background: {color}; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <h3 style="color: white; text-align: center;">{title}</h3>
            <div style="display: flex; justify-content: center;">
                <audio controls style="width: 100%;">
                    <source src="data:audio/mp3;base64,{base64.b64encode(audio_bytes).decode()}" type="audio/mp3">
                </audio>
            </div>
        </div>
        """, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"No se encontró el archivo {audio_file}")

# CSS personalizado
st.markdown("""
<style>
    /* Estilo para el encabezado */
    .header {
        background: linear-gradient(90deg, #1abc9c, #3498db);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* Animación para el título */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .pulse-animation {
        animation: pulse 2s infinite;
        display: inline-block;
    }
    
    /* Estilo para las pestañas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0 20px;
        background-color: #E8F8F5;
        border-radius: 10px 10px 0 0;
        font-weight: bold;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #16A085;
        color: white;
    }
    
    /* Estilo para los versos */
    .verse {
        background-color: #EAF2F8;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    .chorus {
        background-color: #D5F5E3;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 5px solid #16A085;
    }
    
    /* Efecto hover para los elementos interactivos */
    .interactive:hover {
        transform: scale(1.02);
        transition: transform 0.3s ease;
    }
    
    /* Estilo para la imagen de información */
    .info-img {
        width: 100%;
        max-width: 400px;
        border-radius: 10px;
        margin: 15px auto;
        display: block;
    }
    
    /* Estilo para el sidebar */
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado con efecto
st.markdown("""
<div class="header">
    <h1 style="color: white;"><span class="pulse-animation">🎤</span> RAP para AFORE PENSIONISSSTE</h1>
    <p style="color: white; font-size: 1.2em;">Autor: Javier Horacio Pérez Ricárdez</p>
    <p style="color: white; font-size: 1.2em;">¡Tu futuro en ritmo y rima!</p>
</div>
""", unsafe_allow_html=True)

# Columnas para los reproductores
col1, col2 = st.columns(2)

with col1:
    styled_audio_player("PENSIONISSSTE_a.mp3", "Versión A 🎧", "#3498DB")
    st.image("https://cdn.pixabay.com/photo/2017/01/31/23/42/decorative-2028039_640.png", 
            use_container_width=True, caption="Ondas de audio - Versión A")

with col2:
    styled_audio_player("PENSIONISSSTE_b.mp3", "Versión B 🎶", "#9B59B6")
    st.image("https://cdn.pixabay.com/photo/2017/01/31/23/42/decorative-2028039_640.png", 
            use_container_width=True, caption="Ondas de audio - Versión B")

# Letra de la canción con pestañas
st.markdown("---")
tab1, tab2 = st.tabs(["📜 Letra Completa", "🎤 Karaoke"])

with tab1:
    st.markdown("""
    <div style="background-color: #F9F9F9; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <h3 style="color: #E74C3C; text-align: center;">RAP para AFORE PENSIONISSSTE</h3>
        
        <div class="verse">
            <h4 style="color: #2980B9;">Verso 1:</h4>
            <p>Afore PensionISSSTE, ¡es hora de empezar!<br>
            Pensando en tu futuro, con un plan de verdad.<br>
            Ahorra con nosotros, que aquí vas a brillar,<br>
            Tu pensión es segura, la vas a disfrutar.</p>
            
            <p>Cuidamos tu dinero, con amor y rigor,<br>
            Generando rendimientos, con todo el valor.<br>
            Invertimos en grande, no hay error,<br>
            Con Afore PensionISSSTE, no hay temor.</p>
        </div>
        
        <div class="chorus">
            <h4 style="color: #16A085;">Coro:</h4>
            <p>Afore PENSIONISSSTE, tu futuro en acción,<br>
            Ahorra con nosotros, que tenemos la solución.<br>
            Rendimiento constante, no hay confusión,<br>
            ¡Haz crecer tu pensión, con esta misión!</p>
        </div>
        
        <div class="verse">
            <h4 style="color: #2980B9;">Verso 2:</h4>
            <p>El servicio es claro, directo y fiel,<br>
            Te damos opciones, con un trato bien.<br>
            Desde el principio, te cuidamos bien,<br>
            La pensión que soñaste, la verás también.</p>
            
            <p>Si te unes a nosotros, no te vas a arrepentir,<br>
            Tu futuro asegurado, sin tener que sufrir.<br>
            Con Afore PensionISSSTE, todo es fácil de entender,<br>
            Aquí tu dinero crece, ¡no hay por qué temer!</p>
        </div>
        
        <div class="chorus">
            <h4 style="color: #16A085;">Coro (Repetición):</h4>
            <p>Afore PENSIONISSSTE, tu futuro en acción,<br>
            Ahorra con nosotros, que tenemos la solución.<br>
            Rendimiento constante, no hay confusión,<br>
            ¡Haz crecer tu pensión, con esta misión!</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h3 style="color: #E74C3C;">🎤 Karaoke Time! 🎤</h3>
        <p>¡Sigue la letra mientras suena la música!</p>
        <div style="height: 10px;"></div>
        <img src="https://cdn.pixabay.com/photo/2016/11/22/19/15/microphone-1850121_640.jpg" style="width: 100%; max-width: 400px; border-radius: 10px;" class="interactive">
    </div>
    """, unsafe_allow_html=True)
    
    # Simulador de karaoke con colores que cambian
    lyrics = [
        ("Afore PensionISSSTE, ¡es hora de empezar!", "#3498DB", "verse"),
        ("Pensando en tu futuro, con un plan de verdad.", "#3498DB", "verse"),
        ("Ahorra con nosotros, que aquí vas a brillar,", "#3498DB", "verse"),
        ("Tu pensión es segura, la vas a disfrutar.", "#3498DB", "verse"),
        ("", "", ""),
        ("Cuidamos tu dinero, con amor y rigor,", "#3498DB", "verse"),
        ("Generando rendimientos, con todo el valor.", "#3498DB", "verse"),
        ("Invertimos en grande, no hay error,", "#3498DB", "verse"),
        ("Con Afore PensionISSSTE, no hay temor.", "#3498DB", "verse"),
        ("", "", ""),
        ("Afore PENSIONISSSTE, tu futuro en acción,", "#16A085", "chorus"),
        ("Ahorra con nosotros, que tenemos la solución.", "#16A085", "chorus"),
        ("Rendimiento constante, no hay confusión,", "#16A085", "chorus"),
        ("¡Haz crecer tu pensión, con esta misión!", "#16A085", "chorus"),
    ]
    
    for line, color, line_type in lyrics:
        if line:
            if line_type == "chorus":
                st.markdown(f'<div class="chorus" style="padding: 10px; margin: 5px 0;"><p style="font-size: 20px; color: {color}; text-align: center;">{line}</p></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<p style="font-size: 18px; color: {color}; text-align: center;">{line}</p>', unsafe_allow_html=True)
        else:
            st.write("")

# Sección de información adicional
st.markdown("---")
expander = st.expander("ℹ️ Más información sobre AFORE PENSIONISSSTE")
with expander:
    st.markdown("""
    <div style="background-color: #F0F2F6; padding: 20px; border-radius: 10px;">
        <h3 style="color: #2980B9;">AFORE PENSIONISSSTE</h3>
        <p>Es una Administradora de Fondos para el Retiro que ofrece:</p>
        <ul>
            <li>📈 Rendimientos competitivos</li>
            <li>🔒 Seguridad en tus inversiones</li>
            <li>👤 Atención personalizada</li>
            <li>💼 Diversas opciones de ahorro</li>
        </ul>
        <p>¡Comienza a planear tu retiro hoy mismo con el ritmo del RAP PENSIONISSSTE!</p>
        <img class="info-img" src="https://cdn.pixabay.com/photo/2017/01/13/01/22/retirement-1976610_640.jpg" alt="Jubilación feliz">
    </div>
    """, unsafe_allow_html=True)

# Efectos visuales
st.balloons()
