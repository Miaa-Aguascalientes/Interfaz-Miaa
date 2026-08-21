import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Modelo Integral de Aguas de Aguascalientes",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

query_params = st.query_params
vista_actual = query_params.get("vista", "home")

# CSS para recortar el iframe y ocultar el footer "Built with Streamlit"
css_ancho_total = ""
if vista_actual != 'home':
    css_ancho_total = """
    .block-container {
        max-width: 100% !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
    }
    
    /* Contenedor con overflow hidden para cortar la parte inferior del iframe donde sale el footer */
    .iframe-crop-container {
        width: 100%;
        height: 890px;
        overflow: hidden;
        position: relative;
    }
    
    .iframe-crop-container iframe {
        width: 100%;
        height: 960px;
        border: none;
        position: absolute;
        top: 0;
        left: 0;
    }
    """

st.markdown(f"""
    <style>
    .stApp {{
        background-color: #070D19;
        color: #FFFFFF;
        font-family: 'sans-serif';
        overflow-x: hidden;
    }}
    
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    .block-container {{
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        max-width: 100% !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }}

    .wave-background {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 0;
        pointer-events: none;
        background: radial-gradient(circle at 50% 20%, #0A1931 0%, #070D19 70%);
        overflow: hidden;
    }}
    
    .wave {{
        position: absolute;
        bottom: 0;
        left: 0;
        width: 200%;
        height: 100%;
        background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none"><path d="M0,0 C150,90 350,-40 500,40 C650,120 900,20 1200,60 L1200,120 L0,120 Z" fill="rgba(0, 168, 255, 0.04)"/></svg>');
        background-repeat: repeat-x;
        animation: wave-animation 15s linear infinite;
    }}
    
    .wave:nth-of-type(2) {{
        bottom: 10px;
        opacity: 0.5;
        animation: wave-animation 25s linear infinite reverse;
        background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none"><path d="M0,30 C200,100 400,0 600,50 C800,100 1000,10 1200,40 L1200,120 L0,120 Z" fill="rgba(0, 168, 255, 0.03)"/></svg>');
    }}

    @keyframes wave-animation {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(-50%); }}
    }}

    .main-content {{
        position: relative;
        z-index: 10;
        max-width: 700px;
        margin: 0 auto;
    }}

    .grid-container {{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
        margin-bottom: 12px;
    }}
    
    .custom-card {{
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
    }}
    
    .custom-card:hover {{
        border-color: #00A8FF;
        transform: translateY(-2px);
    }}
    
    .status-card {{
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
    }}
    
    .welcome-title {{
        font-size: 24px;
        font-weight: 700;
        color: #FFFFFF;
        margin-top: 5px;
        margin-bottom: 2px;
    }}
    
    .welcome-subtitle {{
        font-size: 13px;
        color: #94A3B8;
        margin-bottom: 12px;
    }}
    
    .card-title {{
        font-size: 13px;
        font-weight: 600;
        color: #FFFFFF;
        margin-top: 4px;
        margin-bottom: 4px;
    }}
    
    .card-desc {{
        font-size: 10px;
        color: #94A3B8;
        margin-bottom: 10px;
        line-height: 1.2;
    }}
    
    .card-button {{
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
    }}
    
    .card-button:hover {{
        background-color: #00A8FF;
        color: #FFFFFF;
    }}
    
    .footer-links {{
        text-align: center;
        color: #64748B;
        font-size: 11px;
        margin-top: 10px;
    }}
    
    .footer-links a {{
        color: #38BDF8;
        text-decoration: none;
    }}

    .stButton > button {{
        background-color: #132238 !important;
        border: 1px solid #00A8FF !important;
        color: #38BDF8 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        width: 100% !important;
    }}
    .stButton > button:hover {{
        background-color: #00A8FF !important;
        color: #FFFFFF !important;
    }}

    {css_ancho_total}
    </style>

    <div class="wave-background">
        <div class="wave"></div>
        <div class="wave"></div>
    </div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# VISTA PRINCIPAL (HOME)
# -------------------------------------------------------------------------
if vista_actual == 'home':
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    logo_url = "https://raw.githubusercontent.com/Miaa-Aguascalientes/Logos/38504978c8f77a4dac38ad476f74dbdee6af2cad/LogoMIAA.svg"
    st.markdown(f'<div style="text-align: center; padding-top: 0px;"><img src="{logo_url}" width="140px" alt="Logo MIAA"><p style="color: #94A3B8; font-size: 10px; margin-top: 2px;">Sistema integral de Aguascalientes</p></div>', unsafe_allow_html=True)

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
    </div>
    """
    st.markdown(cards_html, unsafe_allow_html=True)

    st.markdown("""
        <div class="status-card">
            <div style="display: flex; align-items: center; gap: 8px;">
                <div style="font-size: 20px; color: #38BDF8;">🛡️</div>
                <div>
                    <div style="font-size: 12px; font-weight: 600; color: #FFFFFF;">Seguridad y confiabilidad</div>
                    <div style="font-size: 9px; color: #94A3B8;">Protegemos la información y la disponibilidad</div>
                </div>
            </div>
            <div style="text-align: right; min-width: 80px;">
                <span style="height: 6px; width: 6px; background-color: #22C55E; border-radius: 50%; display: inline-block; margin-right: 3px;"></span>
                <span style="font-size: 9px; color: #22C55E; font-weight: 500;">Sistema en línea</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    current_year = date.today().year
    st.markdown(f"""
        <div class="footer-links">
            🔒 <a href="#">Política de privacidad</a><br>
            © {current_year} MIAA. Todos los derechos reservados.
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------------------
# VISTA INTERNA
# -------------------------------------------------------------------------
else:
    col_back, col_space = st.columns([2, 5])
    with col_back:
        if st.button("⬅️ Volver al menú principal"):
            st.query_params.clear()
            st.rerun()

    urls = {
        'registro': "https://registro-de-usuarios.streamlit.app/?embed=true",
        'scada': "https://sistema-scada-smartphone.streamlit.app/?embed=true",
        'op': "https://telegram-scada.streamlit.app/?embed=true",
        'eventos': "https://incidencias-en-sitios-miaa.streamlit.app/?embed=true"
    }

    url_activa = urls.get(vista_actual)
    if url_activa:
        st.markdown('<div class="iframe-crop-container">', unsafe_allow_html=True)
        st.components.v1.iframe(url_activa, height=960, scrolling=True)
        st.markdown('</div>', unsafe_allow_html=True)
