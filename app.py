# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 12:15:26 2025

@author: jperezr
"""

import streamlit as st
import base64

# Configuración de la página
st.set_page_config(
    page_title="RAP DEL RETIRO",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar con información del autor
with st.sidebar:
    st.title("Créditos")
    st.markdown("---")
    st.markdown("""
    **Javier Horacio Pérez Ricárdez**  
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
    <h1 style="color: white;"><span class="pulse-animation">🎤</span> Las 10 AFORE - RAP del Retiro</h1>
    <p style="color: white; font-size: 1.2em;">Autor: Javier Horacio Pérez Ricárdez</p>
    <p style="color: white; font-size: 1.2em;">¡Elige bien tu AFORE con ritmo!</p>
</div>
""", unsafe_allow_html=True)

# Columnas para los reproductores
col1, col2 = st.columns(2)

with col1:
    styled_audio_player("AFORE_RAP_a.mp3", "Versión A 🎧", "#3498DB")
    st.image("https://cdn.pixabay.com/photo/2017/01/31/23/42/decorative-2028039_640.png", 
            use_container_width=True, caption="Ondas de audio - Versión A")

with col2:
    styled_audio_player("AFORE_RAP_b.mp3", "Versión B 🎶", "#9B59B6")
    st.image("https://cdn.pixabay.com/photo/2017/01/31/23/42/decorative-2028039_640.png", 
            use_container_width=True, caption="Ondas de audio - Versión B")

# Letra de la canción con pestañas
st.markdown("---")
tab1, tab2 = st.tabs(["📜 Letra Completa", "🎤 Karaoke"])

with tab1:
    st.markdown("""
    <div style="background-color: #F9F9F9; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <h3 style="color: #E74C3C; text-align: center;">Las 10 AFORE - RAP del Retiro</h3>
        
        <div class="verse">
            <h4 style="color: #2980B9;">Intro:</h4>
            <p>(Yeah, yeah, ajá...)<br>
            Diez AFORE en el juego, pon atención,<br>
            elige bien pa' tu jubilación.<br>
            No es un juego, es inversión,<br>
            piensa en el viejo que serás, campeón.</p>
        </div>
        
        <div class="verse">
            <h4 style="color: #2980B9;">Verso 1:</h4>
            <p>AFORE Azteca llega y te reta,<br>
            Citibanamex con la cuenta completa.<br>
            Coppel te dice "ven, te conviene",<br>
            Inbursa calcula lo que te mantiene.<br>
            Invercap suma, rendimiento a la luna,<br>
            PENSIONISSSTE firme, nunca se esfuma.<br>
            Principal te enseña a ahorrar,<br>
            Profuturo pa'l retiro y descansar.</p>
        </div>
        
        <div class="chorus">
            <h4 style="color: #16A085;">Coro:</h4>
            <p>(Ey, ey, cuál vas a escoger? 🎤)<br>
            Sura y XX-Banorte también hay que ver.<br>
            (Ey, ey, tu dinero a crecer)<br>
            Pa' que cuando envejezcas la pases de 10.</p>
        </div>
        
        <div class="verse">
            <h4 style="color: #2980B9;">Verso 2:</h4>
            <p>No te duermas, no lo dejes al azar,<br>
            checa la tasa antes de firmar.<br>
            Si la comisión te come la pensión,<br>
            cuando te jubiles dirás "qué error".<br>
            Mueve tu cuenta, revisa el trato,<br>
            piensa en el sueldo del viejito en el banco.<br>
            Ahorra temprano, retírate sano,<br>
            no dejes que el tiempo te gane la mano.</p>
        </div>
        
        <div class="verse">
            <h4 style="color: #2980B9;">Puente:</h4>
            <p>(Yeah, yeah, suéltalo DJ! 🎶🔥)<br>
            Si no comparas, luego llorarás,<br>
            el retiro es serio, no improvisarás.</p>
        </div>
        
        <div class="chorus">
            <h4 style="color: #16A085;">Coro (Repetición):</h4>
            <p>(Ey, ey, cuál vas a escoger? 🎤)<br>
            Sura y XX-Banorte también hay que ver.<br>
            (Ey, ey, tu dinero a crecer)<br>
            Pa' que cuando envejezcas la pases de 10.</p>
        </div>
        
        <div class="verse">
            <h4 style="color: #2980B9;">Outro:</h4>
            <p>(Yeah, yeah... ¡AFORE, AFORE, toma el control!)<br>
            Hazlo ahora, no dejes el goal.<br>
            Que el futuro no espera,<br>
            y en la vejez... ¡no hay replay! 🎤🔥</p>
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
        ("(Yeah, yeah, ajá...)", "#9B59B6", "verse"),
        ("Diez AFORE en el juego, pon atención,", "#9B59B6", "verse"),
        ("elige bien pa' tu jubilación.", "#9B59B6", "verse"),
        ("No es un juego, es inversión,", "#9B59B6", "verse"),
        ("piensa en el viejo que serás, campeón.", "#9B59B6", "verse"),
        ("", "", ""),
        ("AFORE Azteca llega y te reta,", "#3498DB", "verse"),
        ("Citibanamex con la cuenta completa.", "#3498DB", "verse"),
        ("Coppel te dice 'ven, te conviene',", "#3498DB", "verse"),
        ("Inbursa calcula lo que te mantiene.", "#3498DB", "verse"),
        ("Invercap suma, rendimiento a la luna,", "#3498DB", "verse"),
        ("PENSIONISSSTE firme, nunca se esfuma.", "#3498DB", "verse"),
        ("Principal te enseña a ahorrar,", "#3498DB", "verse"),
        ("Profuturo pa'l retiro y descansar.", "#3498DB", "verse"),
        ("", "", ""),
        ("(Ey, ey, cuál vas a escoger? 🎤)", "#16A085", "chorus"),
        ("Sura y XX-Banorte también hay que ver.", "#16A085", "chorus"),
        ("(Ey, ey, tu dinero a crecer)", "#16A085", "chorus"),
        ("Pa' que cuando envejezcas la pases de 10.", "#16A085", "chorus"),
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
expander = st.expander("ℹ️ Información sobre las AFORE en México")
with expander:
    st.markdown("""
    <div style="background-color: #F0F2F6; padding: 20px; border-radius: 10px;">
        <h3 style="color: #2980B9;">¿Qué es una AFORE?</h3>
        <p>Las AFORE (Administradoras de Fondos para el Retiro) son instituciones financieras que:</p>
        <ul>
            <li>📈 Administran tus ahorros para el retiro</li>
            <li>🔒 Ofrecen seguridad y rendimientos</li>
            <li>👤 Permiten comparar comisiones y rendimientos</li>
            <li>💼 Te ayudan a planear tu futuro financiero</li>
        </ul>
        <p>¡Compara y elige la mejor AFORE para tu retiro con el ritmo del RAP!</p>
        <img class="info-img" src="https://cdn.pixabay.com/photo/2017/07/31/11/21/people-2557399_640.jpg" alt="Personas planeando su retiro">
    </div>
    """, unsafe_allow_html=True)

# Efectos visuales
st.balloons()
