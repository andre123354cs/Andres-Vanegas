import streamlit as st

st.set_page_config(layout="wide")

imagen_perfil = "https://media.licdn.com/dms/image/v2/D4E03AQEJOCsUNzF9rw/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1712973716317?e=1738800000&v=beta&t=HPuQ9s25HudkUSBEHLYVsaBXbD39HazKqrLCTkwKEx4"

st.image(imagen_perfil, width=250)
st.title("Andrés Vanegas")
st.subheader("Técnico en Sistemas | Administrador de Empresas")
st.write("Telefono | 3145594483")
st.write("Mail | Edwar.vaco@gmail.com")

st.write("Coordinador de Inteligencia Empresarial. | Extracción de datos, Preprocesamiento, Modelado, Algoritmos, Aprendizaje automático, Clasificación, Agrupamiento, Análisis de patrones, Minería de texto Y Visualización de datos.")
st.write("________________________________________________________________________________________________")

st.markdown("Técnico altamente capacitado en el análisis de datos y la optimización de procesos, con una sólida experiencia en el sector aeronáutico y el transporte aéreo de carga. Con más de dos años de experiencia, he demostrado habilidades excepcionales en la recopilación, análisis e interpretación de datos para impulsar la toma de decisiones estratégicas y mejorar la eficiencia operativa. Recientemente, me he inclinado como coordinador BI sobre negocios de cartera, optimizando la gestión y análisis de portafolios para maximizar su rendimiento")

# Habilidades
st.header("Habilidades")
st.write("""
* **Desarrollo:** Python, JavaScript, HTML, CSS, React
* **Bases de datos:** SQL, PostgreSQL
* **Herramientas:** Git, Docker, AWS
* **Blandas:** Trabajo en equipo, resolución de problemas, comunicación efectiva
""")

# Proyectos
st.header("Proyectos")
st.write("""
* **Proyecto 1:** Breve descripción del proyecto 1, tecnologías utilizadas, resultados obtenidos.
* **Proyecto 2:** Breve descripción del proyecto 2, tecnologías utilizadas, resultados obtenidos.
""")

# Contacto
st.header("Contacto")
st.write("""
* **Correo electrónico:** andres.vanegas@example.com
* **LinkedIn:** https://www.linkedin.com/in/andres-vanegas/
* **GitHub:** https://github.com/andresvanegas
""")

# Imagen de perfil (opcional)
if st.checkbox("Mostrar imagen de perfil"):
    st.image("tu_foto.jpg")
