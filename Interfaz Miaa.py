import streamlit as st

# Configuración de la página para adaptar el diseño
st.set_page_config(
    page_title="Modelo Integral de Aguas de Aguascalientes",
    page_icon="💧",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilos CSS personalizados para replicar la interfaz oscura, tarjetas y tipografía
st.markdown("""
    <style>
    /* Fondo general de la aplicación */
    .stApp {
        background-color: #070D19;
        color: #FFFFFF;
        font-family: 'sans-serif';
    }
    
    /* Ocultar elementos predeterminados de Streamlit para una vista más limpia tipo app */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Contenedor de las tarjetas estilo "Card" */
    .custom-card {
        background-color: #0D172B;
        border: 1px solid #1E2D4A;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin-bottom: 16px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    
    .custom-card:hover {
        border-color: #00A8FF;
        transform: translateY(-2px);
    }

    /* Tarjeta inferior de estado */
    .status-card {
        background-color: #0D172B;
        border: 1px solid #1E2D4A;
        border-radius: 16px;
        padding: 16px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 10px;
        margin-bottom: 20px;
    }

    /* Estilos de textos */
    .welcome-title {
        font-size: 28px;
        font-weight: 700;
        color: #FFFFFF;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    
    .welcome-subtitle {
        font-size: 14px;
        color: #94A3B8;
        margin-bottom: 25px;
    }

    .card-title {
        font-size: 16px;
        font-weight: 600;
        color: #FFFFFF;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .card-desc {
        font-size: 12px;
        color: #94A3B8;
        margin-bottom: 15px;
        min-height: 35px;
    }

    /* Estilo para los enlaces de los botones */
    .card-button {
        display: inline-flex;
        justify-content: center;
        align-items: center;
        width: 36px;
        height: 36px;
        background-color: #132238;
        border: 1px solid #1E3A60;
        border-radius: 50%;
        color: #38BDF8;
        text-decoration: none;
        font-size: 16px;
        transition: background-color 0.2s;
    }

    .card-button:hover {
        background-color: #00A8FF;
        color: #FFFFFF;
    }
    
    /* Footer links */
    .footer-links {
        text-align: center;
        color: #64748B;
        font-size: 12px;
        margin-top: 20px;
    }
    
    .footer-links a {
        color: #38BDF8;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Logotipo de la empresa
logo_url = "https://raw.githubusercontent.com/Miaa-Aguascalientes/Logos/38504978c8f77a4dac38ad476f74dbdee6af2cad/LogoMIAA.svg"
st.markdown(f"""
    <div style="text-align: center; padding-top: 10px;">
        <img src="{logo_url}" width="180px" alt="Logo MIAA">
        <p style="color: #64748B; font-size: 11px; margin-top: 5px; letter-spacing: 0.5px;">Modelo Integral de Aguas de Aguascalientes</p>
    </div>
""", unsafe_allow_html=True)

# 2. Encabezado de bienvenida
st.markdown("""
    <div>
        <div class="welcome-title">¡Bienvenido!</div>
        <div class="welcome-subtitle">Selecciona una opción para continuar</div>
    </div>
""", unsafe_allow_html=True)

# Define aquí las URLs que abrirá cada botón
url_registro = "https://tu-enlace-registro.com"
url_scada = "https://tu-enlace-scada.com"
url_op = "https://tu-enlace-consola.com"
url_eventos = "https://tu-enlace-eventos.com"

# 3. Cuadrícula de 2 columnas para el diseño adaptable (Móvil y Escritorio)
col1, col2 = st.columns(2)

with col1:
    # Tarjeta 1: Registro de usuarios
    st.markdown(f"""
        <div class="custom-card">
            <div style="font-size: 32px; color: #00A8FF; margin-bottom: 5px;">👤➕</div>
            <div class="card-title">Registro de usuarios</div>
            <div class="card-desc">Administra y registra nuevos usuarios del sistema</div>
            <a href="{url_registro}" target="_blank" class="card-button">➔</a>
        </div>
    """, unsafe_allow_html=True)

    # Tarjeta 3: Consola de OP
    st.markdown(f"""
        <div class="custom-card">
            <div style="font-size: 32px; color: #00A8FF; margin-bottom: 5px;">🖥️📈</div>
            <div class="card-title">Consola de OP</div>
            <div class="card-desc">Visualiza y controla la operación del sistema</div>
            <a href="{url_op}" target="_blank" class="card-button">➔</a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # Tarjeta 2: Sistema Scada
    st.markdown(f"""
        <div class="custom-card">
            <div style="font-size: 32px; color: #00A8FF; margin-bottom: 5px;">💧📊</div>
            <div class="card-title">Sistema Scada</div>
            <div class="card-desc">Monitorea en tiempo real pozos, tanques y equipos</div>
            <a href="{url_scada}" target="_blank" class="card-button">➔</a>
        </div>
    """, unsafe_allow_html=True)

    # Tarjeta 4: Eventos operativos
    st.markdown(f"""
        <div class="custom-card">
            <div style="font-size: 32px; color: #F59E0B; margin-bottom: 5px;">⚠️</div>
            <div class="card-title">Eventos operativos</div>
            <div class="card-desc">Consulta eventos, alertas e incidencias del sistema</div>
            <a href="{url_eventos}" target="_blank" class="card-button">➔</a>
        </div>
    """, unsafe_allow_html=True)

# 4. Tarjeta inferior de Seguridad y confiabilidad
st.markdown("""
    <div class="status-card">
        <div style="display: flex; align-items: center; gap: 12px;">
            <div style="font-size: 24px; color: #38BDF8;">🛡️</div>
            <div>
                <div style="font-size: 14px; font-weight: 600; color: #FFFFFF;">Seguridad y confiabilidad</div>
                <div style="font-size: 11px; color: #94A3B8;">Protegemos la información y garantizamos la disponibilidad del sistema</div>
            </div>
        </div>
        <div style="text-align: right; min-width: 90px;">
            <span style="height: 8px; width: 8px; background-color: #22C55E; border-radius: 50%; display: inline-block; margin-right: 4px;"></span>
            <span style="font-size: 11px; color: #22C55E; font-weight: 500;">Sistema en línea</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. Pie de página (Política de privacidad y Copyright)
st.markdown("""
    <div class="footer-links">
        🔒 <a href="#" target="_blank">Política de privacidad</a><br><br>
        © 2026 MIAA. Todos los derechos reservados.
    </div>
""", unsafe_allow_html=True)
