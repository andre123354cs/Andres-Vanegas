import streamlit as st

# Define el título de la página
st.title('👋 ¡Hola desde Streamlit!')

# Pide al usuario que ingrese su nombre en un campo de texto
nombre_usuario = st.text_input('Por favor, ingresa tu nombre:', '')

# Muestra un mensaje personalizado si el usuario ha escrito su nombre
if nombre_usuario:
    st.write(f'¡Bienvenido, {nombre_usuario}!')
    st.balloons()
