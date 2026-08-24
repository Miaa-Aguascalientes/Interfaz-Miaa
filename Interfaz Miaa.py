import streamlit as st

st.set_page_config(
    page_title="Modelo Integral de Aguas de Aguascalientes",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos limpios y profesionales
st.markdown("""
    <style>
    .stApp { background-color: #050a10 !important; color: #FFFFFF; font-family: 'sans-serif'; overflow-x: hidden; }
    header, footer, [data-testid="stStatusWidget"], #MainMenu, .viewerBadge_container, div[class*="viewerBadge"] {
        display: none !important;
        visibility: hidden !important;
    }

    .wave-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 0;
        pointer-events: none;
        background: radial-gradient(circle at 50% 20%, #0A1931 0%, #050a10 70%);
        overflow: hidden;
    }
    
    .wave {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 200%;
        height: 100%;
        background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none"><path d="M0,0 C150,90 350,-40 500,40 C650,120 900,20 1200,60 L1200,120 L0,120 Z" fill="rgba(0, 168, 255, 0.04)"/></svg>');
        background-repeat: repeat-x;
        animation: wave-animation 15s linear infinite;
    }
    
    .wave:nth-of-type(2) {
        bottom: 10px;
        opacity: 0.5;
        animation: wave-animation 25s linear infinite reverse;
        background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none"><path d="M0,30 C200,100 400,0 600,50 C800,100 1000,10 1200,40 L1200,120 L0,120 Z" fill="rgba(0, 168, 255, 0.03)"/></svg>');
    }

    @keyframes wave-animation {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }

    .main-content {
        position: relative;
        z-index: 10;
        max-width: 700px;
        margin: 0 auto;
        padding: 10px;
    }

    .status-card {
        background-color: rgba(13, 23, 43, 0.85);
        border: 1px solid #1E2D4A;
        border-radius: 16px;
        padding: 12px 16px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 15px;
        margin-bottom: 10px;
        backdrop-filter: blur(8px);
    }
    
    .welcome-title {
        font-size: 24px;
        font-weight: 700;
        color: #FFFFFF;
        margin-top: 0px;
        margin-bottom: 2px;
    }
    
    .welcome-subtitle {
        font-size: 13px;
        color: #94A3B8;
        margin-bottom: 15px;
    }
    </style>

    <div class="wave-background">
        <div class="wave"></div>
        <div class="wave"></div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-content">', unsafe_allow_html=True)

logo_url = "https://raw.githubusercontent.com/Miaa-Aguascalientes/Logos/38504978c8f77a4dac38ad476f74dbdee6af2cad/LogoMIAA.svg"
st.markdown(f'<div style="text-align: center; padding-top: 0px;"><img src="{logo_url}" width="130px" alt="Logo MIAA"><p style="color: #94A3B8; font-size: 10px; margin-top: 2px;">Sistema integral de Aguascalientes</p></div>', unsafe_allow_html=True)

st.markdown('<div class="welcome-title">¡Bienvenido!</div><div class="welcome-subtitle">Selecciona una opción para continuar</div>', unsafe_allow_html=True)

# URLs de las aplicaciones
url_registro = "https://registro-de-usuarios.streamlit.app/"
url_scada = "https://sistema-scada-smartphone.streamlit.app/"
url_op = "https://telegram-scada.streamlit.app/"
url_eventos = "https://incidencias-en-sitios-miaa.streamlit.app/"
url_telegram = "https://registro-de-usuarios-telegram.streamlit.app/"

# Usamos columnas nativas con st.link_button para evitar cualquier redirección fantasma o bucle en móviles
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div style="background-color: rgba(13, 23, 43, 0.85); border: 1px solid #1E2D4A; border-radius: 14px; padding: 12px; text-align: center; margin-bottom: 10px; min-height: 160px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <div style="font-size: 22px; margin-bottom: 2px;">👤➕</div>
                <div style="font-size: 13px; font-weight: 600; color: #FFFFFF; margin-bottom: 4px;">Registro de usuarios</div>
                <div style="font-size: 10px; color: #94A3B8; margin-bottom: 8px;">Administra y registra nuevos usuarios</div>
            </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir ➔", url_registro, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
        <div style="background-color: rgba(13, 23, 43, 0.85); border: 1px solid #1E2D4A; border-radius: 14px; padding: 12px; text-align: center; margin-bottom: 10px; min-height: 160px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <div style="font-size: 22px; margin-bottom: 2px;">🖥️📈</div>
                <div style="font-size: 13px; font-weight: 600; color: #FFFFFF; margin-bottom: 4px;">Consola de OP</div>
                <div style="font-size: 10px; color: #94A3B8; margin-bottom: 8px;">Visualiza y controla la operación</div>
            </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir ➔", url_op, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="background-color: rgba(13, 23, 43, 0.85); border: 1px solid #1E2D4A; border-radius: 14px; padding: 12px; text-align: center; margin-bottom: 10px; min-height: 160px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <div style="font-size: 22px; margin-bottom: 2px;">💧📊</div>
                <div style="font-size: 13px; font-weight: 600; color: #FFFFFF; margin-bottom: 4px;">Sistema Scada</div>
                <div style="font-size: 10px; color: #94A3B8; margin-bottom: 8px;">Monitorea pozos y tanques en vivo</div>
            </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir ➔", url_scada, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
        <div style="background-color: rgba(13, 23, 43, 0.85); border: 1px solid #1E2D4A; border-radius: 14px; padding: 12px; text-align: center; margin-bottom: 10px; min-height: 160px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <div style="font-size: 22px; margin-bottom: 2px;">⚠️</div>
                <div style="font-size: 13px; font-weight: 600; color: #FFFFFF; margin-bottom: 4px;">Eventos operativos</div>
                <div style="font-size: 10px; color: #94A3B8; margin-bottom: 8px;">Consulta alertas e incidencias</div>
            </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir ➔", url_eventos, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Tarjeta inferior ancha para Telegram
st.markdown("""
    <div style="background-color: rgba(13, 23, 43, 0.85); border: 1px solid #1E2D4A; border-radius: 14px; padding: 12px; text-align: center; margin-bottom: 10px;">
        <div style="font-size: 22px; margin-bottom: 2px;">💬</div>
        <div style="font-size: 13px; font-weight: 600; color: #FFFFFF; margin-bottom: 4px;">Registro Telegram</div>
        <div style="font-size: 10px; color: #94A3B8; margin-bottom: 8px;">Gestiona altas y notificaciones de Telegram</div>
""", unsafe_allow_html=True)
st.link_button("Abrir Registro Telegram ➔", url_telegram, use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
    <div class="status-card">
        <div style="display: flex; align-items: center; gap: 8px;">
            <div style="font-size: 10px; color: #38BDF8;">🛡️</div>
            <div>
                <div style="font-size: 12px; font-weight: 600; color: #FFFFFF;">Desarrollo. Pedro Guillermo Templos</div>
                <div style="font-size: 9px; color: #94A3B8;">Tecnologia e innovación.</div>
            </div>
        </div>
        <div style="text-align: right; min-width: 80px;">
            <span style="height: 6px; width: 6px; background-color: #22C55E; border-radius: 50%; display: inline-block; margin-right: 3px;"></span>
            <span style="font-size: 9px; color: #22C55E; font-weight: 500;">Sistema en línea</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
