import streamlit as st
import pandas as pd
import cv2
import face_recognition
import os
import numpy as np

# Nombre del archivo para almacenar las codificaciones faciales
REGISTROS_FILE = 'codificaciones_faciales.csv'

def save_encoding(name, encoding):
    """Guarda el nombre y la codificación facial en un archivo CSV."""
    # Convertir el array de numpy a una cadena de texto para guardar
    encoding_str = ','.join(map(str, encoding))
    new_data = pd.DataFrame([{'Nombre': name, 'Codificacion': encoding_str}])
    
    if os.path.exists(REGISTROS_FILE):
        existing_data = pd.read_csv(REGISTROS_FILE)
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        updated_data = new_data
    updated_data.to_csv(REGISTROS_FILE, index=False)

def main_registro():
    """Interfaz para registrar rostros."""
    st.title('Registro de Rostros')
    st.write('Ingresa tu nombre y el sistema capturará tu rostro para el registro.')

    name = st.text_input('Nombre completo')
    
    if st.button('Iniciar Captura'):
        if not name:
            st.warning('Por favor, ingresa un nombre.')
            return

        st.info('Buscando rostro... Asegúrate de estar bien iluminado y de frente a la cámara.')
        
        cap = cv2.VideoCapture(0) # Inicia la cámara
        face_found = False
        
        while not face_found:
            ret, frame = cap.read()
            if not ret:
                continue

            rgb_frame = frame[:, :, ::-1] # Convierte de BGR a RGB
            face_locations = face_recognition.face_locations(rgb_frame)

            if face_locations:
                st.success(f'¡Rostro de {name} detectado!')
                face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]
                save_encoding(name, face_encoding)
                st.success('¡Registro completado! Puedes cerrar la ventana.')
                face_found = True
            
            # Muestra el video en una ventana de OpenCV (no de Streamlit)
            cv2.imshow('Registro de Rostros', frame)
            
            # Rompe el bucle si se presiona 'q' o se detectó el rostro
            if cv2.waitKey(1) & 0xFF == ord('q') or face_found:
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main_registro()
