import streamlit as st

st.set_page_config(
    page_title="Modelo Integral de Aguas de Aguascalientes",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Diccionario con las URLs directas de tus apps
urls = {
    'registro': "https://registro-de-usuarios.streamlit.app/",
    'scada': "https://sistema-scada-smartphone.streamlit.app/",
    'op': "https://telegram-scada.streamlit.app/",
    'eventos': "https://incidencias-en-sitios-miaa.streamlit.app/",
    'telegram': "https://registro-de-usuarios-telegram.streamlit.app/"
}

query_params = st.query_params
vista_actual = query_params.get("vista", "home")

# Si el usuario seleccionó una vista interna, redirigimos limpiamente al sitio externo sin iframe
if vista_actual in urls:
    url_destino = urls[vista_actual]
    # Inyectamos script de redirección inmediata limpia y botón de retorno flotante por si quieren regresar
    st.markdown(f"""
        <style>
            .stApp {{ background-color: #050a10 !important; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; font-family: sans-serif; }}
            header, footer {{ display: none !important; }}
            .loader-box {{ text-align: center; }}
            .btn-regresar {{
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #00A8FF;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
            }}
        </style>
        <div class="loader-box">
            <h3>Abriendo sistema...</h3>
            <p>Si no redirige automáticamente, haz clic abajo:</p>
            <a href="{url_destino}" class="btn-regresar" target="_self">Entrar al sistema</a>
            <br><br>
            <a href="?vista=home" class="btn-regresar" style="background-color: #1E2D4A;" target="_self">← Volver al Inicio</a>
        </div>
        <script>
            // Redirección automática inmediata
            window.location.href = "{url_destino}";
        </script>
    """, unsafe_allow_html=True)
    st.stop()

# -------------------------------------------------------------------------
# VISTA PRINCIPAL (HOME) - Limpia de cualquier porquería de iframes
# -------------------------------------------------------------------------
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

    .grid-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
        margin-bottom: 12px;
    }
    
    .custom-card {
        background-color: rgba(13, 23, 43, 0.85);
        border: 1px solid #1E2D4A;
        border-radius: 14px;
        padding: 14px 10px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 195px;
        backdrop-filter: blur(8px);
        transition: border-color 0.3s, transform 0.2s;
    }
    
    .custom-card:hover {
        border-color: #00A8FF;
        transform: translateY(-2px);
    }
    
    .status-card {
        background-color: rgba(13, 23, 43, 0.85);
        border: 1px solid #1E2D4A;
        border-radius: 16px;
        padding: 12px 16px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 5px;
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
        margin-bottom: 12px;
    }
    
    .card-title {
        font-size: 13px;
        font-weight: 600;
        color: #FFFFFF;
        margin-top: 4px;
        margin-bottom: 4px;
    }
    
    .card-desc {
        font-size: 10px;
        color: #94A3B8;
        margin-bottom: 10px;
        line-height: 1.2;
    }
    
    .card-button {
        display: inline-flex;
        justify-content: center;
        align-items: center;
        width: 30px;
        height: 30px;
        background-color: #132238;
        border: 1px solid #1E3A60;
        border-radius: 50%;
        color: #38BDF8;
        text-decoration: none;
        font-size: 13px;
        margin: 0 auto;
        cursor: pointer;
        transition: background-color 0.3s, color 0.3s;
    }
    
    .card-button:hover {
        background-color: #00A8FF;
        color: #FFFFFF;
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

cards_html = """
<div class="grid-container">
    <div class="custom-card">
        <div>
            <div style="font-size: 24px; color: #00A8FF; margin-bottom: 2px;">👤➕</div>
            <div class="card-title">Registro de usuarios</div>
            <div class="card-desc">Administra y registra nuevos usuarios del sistema</div>
        </div>
        <div><a href="?vista=registro" target="_self" class="card-button">➔</a></div>
    </div>
    <div class="custom-card">
        <div>
            <div style="font-size: 24px; color: #00A8FF; margin-bottom: 2px;">💧📊</div>
            <div class="card-title">Sistema Scada</div>
            <div class="card-desc">Monitorea en tiempo real pozos, tanques y equipos</div>
        </div>
        <div><a href="?vista=scada" target="_self" class="card-button">➔</a></div>
    </div>
    <div class="custom-card">
        <div>
            <div style="font-size: 24px; color: #00A8FF; margin-bottom: 2px;">🖥️📈</div>
            <div class="card-title">Consola de OP</div>
            <div class="card-desc">Visualiza y controla la operación del sistema</div>
        </div>
        <div><a href="?vista=op" target="_self" class="card-button">➔</a></div>
    </div>
    <div class="custom-card">
        <div>
            <div style="font-size: 24px; color: #F59E0B; margin-bottom: 2px;">⚠️</div>
            <div class="card-title">Eventos operativos</div>
            <div class="card-desc">Consulta eventos, alertas e incidencias del sistema</div>
        </div>
        <div><a href="?vista=eventos" target="_self" class="card-button">➔</a></div>
    </div>
    <div class="custom-card" style="grid-column: span 2;">
        <div>
            <div style="margin-bottom: 4px;"><img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" width="28px" alt="Logo Telegram" style="vertical-align: middle;"></div>
            <div class="card-title">Registro Telegram</div>
            <div class="card-desc">Gestiona altas y notificaciones vinculadas a Telegram</div>
        </div>
        <div><a href="?vista=telegram" target="_self" class="card-button">➔</a></div>
    </div>
</div>
"""
st.markdown(cards_html, unsafe_allow_html=True)

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
