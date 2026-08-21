import streamlit as st

st.set_page_config(
    page_title="Modelo Integral de Aguas de Aguascalientes",
    page_icon="💧",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .stApp {
        background-color: #070D19;
        color: #FFFFFF;
        font-family: 'sans-serif';
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .grid-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
        margin-bottom: 16px;
    }
    .custom-card {
        background-color: #0D172B;
        border: 1px solid #1E2D4A;
        border-radius: 14px;
        padding: 14px 10px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 195px;
    }
    .custom-card:hover {
        border-color: #00A8FF;
    }
    .status-card {
        background-color: #0D172B;
        border: 1px solid #1E2D4A;
        border-radius: 16px;
        padding: 14px 16px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    .welcome-title {
        font-size: 24px;
        font-weight: 700;
        color: #FFFFFF;
        margin-top: 10px;
        margin-bottom: 2px;
    }
    .welcome-subtitle {
        font-size: 13px;
        color: #94A3B8;
        margin-bottom: 16px;
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
    }
    .card-button:hover {
        background-color: #00A8FF;
        color: #FFFFFF;
    }
    .footer-links {
        text-align: center;
        color: #64748B;
        font-size: 11px;
        margin-top: 20px;
    }
    .footer-links a {
        color: #38BDF8;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# Logotipo
logo_url = "https://raw.githubusercontent.com/Miaa-Aguascalientes/Logos/38504978c8f77a4dac38ad476f74dbdee6af2cad/LogoMIAA.svg"
st.markdown(f'<div style="text-align: center; padding-top: 10px;"><img src="{logo_url}" width="150px" alt="Logo MIAA"><p style="color: #64748B; font-size: 10px; margin-top: 4px;">Modelo Integral de Aguas de Aguascalientes</p></div>', unsafe_allow_html=True)

# Encabezado
st.markdown('<div class="welcome-title">¡Bienvenido!</div><div class="welcome-subtitle">Selecciona una opción para continuar</div>', unsafe_allow_html=True)

# Direcciones web de los botones
url_registro = "https://tu-enlace-registro.com"
url_scada = "https://tu-enlace-scada.com"
url_op = "https://tu-enlace-consola.com"
url_eventos = "https://tu-enlace-eventos.com"

# Cuadrícula compacta de 2 columnas forzada por CSS
cards_html = f"""
<div class="grid-container">
    <div class="custom-card">
        <div>
            <div style="font-size: 24px; color: #00A8FF; margin-bottom: 2px;">👤➕</div>
            <div class="card-title">Registro de usuarios</div>
            <div class="card-desc">Administra y registra nuevos usuarios del sistema</div>
        </div>
        <div><a href="{url_registro}" target="_blank" class="card-button">➔</a></div>
    </div>
    <div class="custom-card">
        <div>
            <div style="font-size: 24px; color: #00A8FF; margin-bottom: 2px;">💧📊</div>
            <div class="card-title">Sistema Scada</div>
            <div class="card-desc">Monitorea en tiempo real pozos, tanques y equipos</div>
        </div>
        <div><a href="{url_scada}" target="_blank" class="card-button">➔</a></div>
    </div>
    <div class="custom-card">
        <div>
            <div style="font-size: 24px; color: #00A8FF; margin-bottom: 2px;">🖥️📈</div>
            <div class="card-title">Consola de OP</div>
            <div class="card-desc">Visualiza y controla la operación del sistema</div>
        </div>
        <div><a href="{url_op}" target="_blank" class="card-button">➔</a></div>
    </div>
    <div class="custom-card">
        <div>
            <div style="font-size: 24px; color: #F59E0B; margin-bottom: 2px;">⚠️</div>
            <div class="card-title">Eventos operativos</div>
            <div class="card-desc">Consulta eventos, alertas e incidencias del sistema</div>
        </div>
        <div><a href="{url_eventos}" target="_blank" class="card-button">➔</a></div>
    </div>
</div>
"""
st.markdown(cards_html, unsafe_allow_html=True)

# Tarjeta de estado inferior
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

# Pie de página
st.markdown("""
    <div class="footer-links">
        🔒 <a href="#" target="_blank">Política de privacidad</a><br><br>
        © 2026 MIAA. Todos los derechos reservados.
    </div>
""", unsafe_allow_html=True)
