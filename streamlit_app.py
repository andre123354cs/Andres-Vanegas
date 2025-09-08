import streamlit as st
import pandas as pd
import os

# Nombre del archivo para almacenar los datos
FILE_NAME = 'datos_contacto.csv'

# Función para guardar los datos
def save_data(nombre, email):
    # Crea un DataFrame de pandas con los nuevos datos
    new_data = pd.DataFrame([{'Nombre': nombre, 'Email': email}])

    # Si el archivo ya existe, lo lee y concatena los nuevos datos
    if os.path.exists(FILE_NAME):
        existing_data = pd.read_csv(FILE_NAME)
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        # Si no existe, los datos nuevos son los únicos
        updated_data = new_data

    # Guarda el DataFrame actualizado en el archivo CSV
    updated_data.to_csv(FILE_NAME, index=False)

# Título y descripción de la aplicación
st.title('Formulario de Contacto')
st.write('Ingresa tus datos para guardarlos en un archivo CSV.')

# Campos de entrada
with st.form(key='contact_form'):
    nombre = st.text_input('Nombre')
    email = st.text_input('Email')
    submit_button = st.form_submit_button('Guardar Datos')

# Si el botón es presionado, llama a la función para guardar
if submit_button:
    if nombre and email:
        save_data(nombre, email)
        st.success('¡Datos guardados correctamente!')
    else:
        st.warning('Por favor, completa todos los campos.')

# Muestra los datos almacenados
if os.path.exists(FILE_NAME):
    st.subheader('Datos Almacenados')
    df = pd.read_csv(FILE_NAME)
    st.dataframe(df)
    
