import streamlit as st
import streamlit.components.v1 as components
from datetime import date

# Configuración de la página
st.set_page_config(
    page_title="Modelo Integral de Aguas de Aguascalientes",
    page_icon="💧",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilos CSS personalizados para la interfaz, colores y tarjetas
st.markdown("""
    <style>
    /* Fondo general transparente para dejar ver la animación */
    .stApp {
        background: transparent;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Contenedor principal del contenido */
    .main-content {
        position: relative;
        z-index: 10;
        padding-top: 10px;
        padding-bottom: 30px;
    }

    /* Cuadrícula de 2 columnas exactas para las 4 tarjetas */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
        margin-bottom: 24px;
    }

    /* Tarjetas individuales */
    .custom-card {
        background-color: rgba(13, 23, 43, 0.85); /* Fondo oscuro semitransparente */
        border: 1px solid #1E2D4A;
        border-radius: 16px;
        padding: 24px 20px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 230px;
        transition: border-color 0.3s, transform 0.2s;
        backdrop-filter: blur(10px); /* Efecto de desenfoque en el fondo de la tarjeta */
    }
    
    .custom-card:hover {
        border-color: #00A8FF;
        transform: translateY(-2px);
    }

    /* Tarjeta inferior de estado */
    .status-card {
        background-color: rgba(13, 23, 43, 0.85);
        border: 1px solid #1E2D4A;
        border-radius: 16px;
        padding: 16px 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 10px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }

    /* Estilos de textos */
    .welcome-title {
        font-size: 32px;
        font-weight: 800;
        color: #FFFFFF;
        margin-top: 15px;
        margin-bottom: 5px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .welcome-subtitle {
        font-size: 16px;
        color: #94A3B8;
        margin-bottom: 35px;
    }

    .card-title {
        font-size: 18px;
        font-weight: 700;
        color: #FFFFFF;
        margin-top: 12px;
        margin-bottom: 6px;
    }

    .card-desc {
        font-size: 13px;
        color: #94A3B8;
        margin-bottom: 18px;
        line-height: 1.4;
    }

    /* Botones de acción */
    .card-button {
        display: inline-flex;
        justify-content: center;
        align-items: center;
        width: 40px;
        height: 40px;
        background-color: #132238;
        border: 1px solid #1E3A60;
        border-radius: 50%;
        color: #38BDF8;
        text-decoration: none;
        font-size: 18px;
        transition: background-color 0.3s, color 0.3s;
        margin: 0 auto;
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
        transition: color 0.3s;
    }
    
    .footer-links a:hover {
        color: #FFFFFF;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Animación de fondo (Partículas dinámicas con Three.js)
# Insertamos un bloque HTML que ocupa toda la pantalla con un fondo animado
bg_html = """
<style>
body, html {
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
    overflow: hidden;
    background-color: #070D19; /* Color de fondo base */
}
#canvas-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
}
</style>
<div id="canvas-container"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
// Three.js Background Animation
const container = document.getElementById('canvas-container');
let scene, camera, renderer, particles;
let mouseX = 0, mouseY = 0;
let windowHalfX = window.innerWidth / 2;
let windowHalfY = window.innerHeight / 2;

function init() {
    scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x070D19, 0.001);

    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 1, 1000);
    camera.position.z = 500;

    particles = new THREE.Geometry();
    const pMaterial = new THREE.PointsMaterial({
        color: 0x0088FF, // Color de las partículas
        size: 2,
        blending: THREE.AdditiveBlending,
        transparent: true,
        opacity: 0.6
    });

    for (let i = 0; i < 8000; i++) {
        const pX = Math.random() * 2000 - 1000;
        const pY = Math.random() * 2000 - 1000;
        const pZ = Math.random() * 2000 - 1000;
        const particle = new THREE.Vector3(pX, pY, pZ);
        particle.velocity = new THREE.Vector3(0, Math.random(), 0);
        particles.vertices.push(particle);
    }

    particleSystem = new THREE.Points(particles, pMaterial);
    scene.add(particleSystem);

    renderer = new THREE.WebGLRenderer({ alpha: true });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(window.innerWidth, window.innerHeight);
    container.appendChild(renderer.domElement);

    document.addEventListener('mousemove', onDocumentMouseMove, false);
    window.addEventListener('resize', onWindowResize, false);
}

function onWindowResize() {
    windowHalfX = window.innerWidth / 2;
    windowHalfY = window.innerHeight / 2;
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

function onDocumentMouseMove(event) {
    mouseX = event.clientX - windowHalfX;
    mouseY = event.clientY - windowHalfY;
}

function animate() {
    requestAnimationFrame(animate);
    render();
}

function render() {
    camera.position.x += (mouseX - camera.position.x) * 0.01;
    camera.position.y += (-mouseY - camera.position.y) * 0.01;
    camera.lookAt(scene.scenePosition);

    particles.vertices.forEach(function(particle) {
        particle.y += particle.velocity.y;
        if (particle.y > 1000) particle.y = -1000;
    });
    
    particleSystem.rotation.y += 0.001;
    particleSystem.rotation.x += 0.001;

    renderer.render(scene, camera);
}

init();
animate();
</script>
"""
# Insertamos el fondo animado
components.html(bg_html, height=1000)


# 2. Contenido principal superpuesto sobre la animación
with st.container():
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    # 2.1 Logotipo de la empresa
    logo_url = "https://raw.githubusercontent.com/Miaa-Aguascalientes/Logos/38504978c8f77a4dac38ad476f74dbdee6af2cad/LogoMIAA.svg"
    st.markdown(f"""
        <div style="text-align: center; padding-top: 10px;">
            <img src="{logo_url}" width="220px" alt="Logo MIAA">
            <p style="color: #94A3B8; font-size: 13px; margin-top: 8px; letter-spacing: 0.5px;">Modelo Integral de Aguas de Aguascalientes</p>
        </div>
    """, unsafe_allow_html=True)

    # 2.2 Encabezado de bienvenida
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

    # 2.3 Cuadrícula de 2 columnas para los botones
    grid_html = f"""
        <div class="grid-container">
            <!-- Tarjeta 1: Registro de usuarios -->
            <div class="custom-card">
                <div>
                    <div style="font-size: 36px; color: #00A8FF; margin-bottom: 10px;">👤➕</div>
                    <div class="card-title">Registro de usuarios</div>
                    <div class="card-desc">Administra y registra nuevos usuarios del sistema</div>
                </div>
                <div>
                    <a href="{url_registro}" target="_blank" class="card-button">➔</a>
                </div>
            </div>

            <!-- Tarjeta 2: Sistema Scada -->
            <div class="custom-card">
                <div>
                    <div style="font-size: 36px; color: #00A8FF; margin-bottom: 10px;">💧📊</div>
                    <div class="card-title">Sistema Scada</div>
                    <div class="card-desc">Monitorea en tiempo real pozos, tanques y equipos</div>
                </div>
                <div>
                    <a href="{url_scada}" target="_blank" class="card-button">➔</a>
                </div>
            </div>

            <!-- Tarjeta 3: Consola de OP -->
            <div class="custom-card">
                <div>
                    <div style="font-size: 36px; color: #00A8FF; margin-bottom: 10px;">🖥️📈</div>
                    <div class="card-title">Consola de OP</div>
                    <div class="card-desc">Visualiza y controla la operación del sistema</div>
                </div>
                <div>
                    <a href="{url_op}" target="_blank" class="card-button">➔</a>
                </div>
            </div>

            <!-- Tarjeta 4: Eventos operativos -->
            <div class="custom-card">
                <div>
                    <div style="font-size: 36px; color: #F59E0B; margin-bottom: 10px;">⚠️</div>
                    <div class="card-title">Eventos operativos</div>
                    <div class="card-desc">Consulta eventos, alertas e incidencias del sistema</div>
                </div>
                <div>
                    <a href="{url_eventos}" target="_blank" class="card-button">➔</a>
                </div>
            </div>
        </div>
    """
    st.markdown(grid_html, unsafe_allow_html=True)

    # 2.4 Tarjeta inferior de Seguridad y confiabilidad
    st.markdown("""
        <div class="status-card">
            <div style="display: flex; align-items: center; gap: 16px;">
                <div style="font-size: 30px; color: #38BDF8;">🛡️</div>
                <div>
                    <div style="font-size: 16px; font-weight: 700; color: #FFFFFF;">Seguridad y confiabilidad</div>
                    <div style="font-size: 13px; color: #94A3B8;">Protegemos la información y garantizamos la disponibilidad del sistema</div>
                </div>
            </div>
            <div style="text-align: right; min-width: 120px; background-color: rgba(16, 185, 129, 0.15); padding: 6px 12px; border-radius: 20px; border: 1px solid rgba(16, 185, 129, 0.3);">
                <span style="height: 10px; width: 10px; background-color: #22C55E; border-radius: 50%; display: inline-block; margin-right: 6px; box-shadow: 0 0 8px #22C55E;"></span>
                <span style="font-size: 14px; color: #22C55E; font-weight: 600;">Sistema en línea</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 2.5 Pie de página
    current_year = date.today().year
    st.markdown(f"""
        <div class="footer-links">
            🔒 <a href="#" target="_blank">Política de privacidad</a><br><br>
            © {current_year} MIAA. Todos los derechos reservados.
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True) # Cierre de main-content
