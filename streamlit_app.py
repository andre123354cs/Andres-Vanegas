import streamlit as st

st.set_page_config(layout="wide")

imagen_perfil = "https://media.licdn.com/dms/image/v2/D4E03AQEJOCsUNzF9rw/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1712973716317?e=1738800000&v=beta&t=HPuQ9s25HudkUSBEHLYVsaBXbD39HazKqrLCTkwKEx4"

st.image(imagen_perfil, width=250)
st.title("Andrés Vanegas")
st.subheader("Técnico en Sistemas | Administrador de Empresas")

st.subheader("Coordinador de Inteligencia Empresarial. | Extracción de datos, Preprocesamiento, Modelado, Algoritmos, Aprendizaje automático, Clasificación, Agrupamiento, Análisis de patrones, Minería de texto Y Visualización de datos.")

st.write("Soy Andrés Vanegas, un apasionado por la tecnología y la administración. Actualmente me encuentro cursando el quinto semestre de Administración de Empresas y soy técnico en sistemas con énfasis en desarrollo.")

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
