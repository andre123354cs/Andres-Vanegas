import streamlit as st
import pandas as pd
import os

# Nombre del archivo para almacenar los datos
FILE_NAME = 'datos_contacto.csv'

# Función para guardar los datos
def save_data(nombre, email):
    new_data = pd.DataFrame([{'Nombre': nombre, 'Email': email}])
    if os.path.exists(FILE_NAME):
        existing_data = pd.read_csv(FILE_NAME)
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        updated_data = new_data
    updated_data.to_csv(FILE_NAME, index=False)

# Título y formulario
st.title('Formulario de Contacto')
st.write('Ingresa tus datos para guardarlos en un archivo CSV.')

with st.form(key='contact_form'):
    nombre = st.text_input('Nombre')
    email = st.text_input('Email')
    submit_button = st.form_submit_button('Guardar Datos')

if submit_button:
    if nombre and email:
        save_data(nombre, email)
        st.success('¡Datos guardados correctamente!')
    else:
        st.warning('Por favor, completa todos los campos.')

# Sección para visualizar y descargar los datos
if os.path.exists(FILE_NAME):
    st.subheader('Datos Almacenados')
    df = pd.read_csv(FILE_NAME)
    st.dataframe(df)

    # Convertir el DataFrame a un formato de cadena de texto (CSV)
    # y crear el botón de descarga
    csv_string = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Descargar datos en CSV",
        data=csv_string,
        file_name='contactos.csv',
        mime='text/csv'
    )
