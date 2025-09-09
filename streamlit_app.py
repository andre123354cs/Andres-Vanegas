import streamlit as st
import pandas as pd
import os

# Nombre del archivo para almacenar los datos de los usuarios
USUARIOS_FILE = 'usuarios.csv'

# --- Funciones de la aplicación ---

def save_user(name, code):
    """Guarda el nombre y el código de acceso del usuario en un archivo CSV."""
    new_data = pd.DataFrame([{'Nombre': name, 'Codigo': code}])
    
    if os.path.exists(USUARIOS_FILE):
        existing_data = pd.read_csv(USUARIOS_FILE)
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        updated_data = new_data
        
    updated_data.to_csv(USUARIOS_FILE, index=False)
    st.success(f"Usuario '{name}' registrado exitosamente.")

def verify_user(name, code):
    """Verifica si el nombre y el código coinciden con un registro existente."""
    if not os.path.exists(USUARIOS_FILE):
        return False, "El archivo de usuarios no existe. Por favor, regístrese primero."
    
    df = pd.read_csv(USUARIOS_FILE)
    
    # Intenta encontrar una fila que coincida con el nombre y el código proporcionados
    match = df[(df['Nombre'] == name) & (df['Codigo'] == code)]
    
    if not match.empty:
        return True, "¡Acceso concedido!"
    else:
        return False, "Nombre de usuario o código incorrectos."

def main():
    """Lógica principal de la aplicación Streamlit."""
    st.set_page_config(layout="wide")
    st.title('Sistema de Acceso de Usuarios')
    st.write('Elige una opción para registrarte o ingresar al sistema.')

    # Usa un radio para alternar entre las vistas de registro y login
    opcion = st.radio("Selecciona una acción:", ('Registrarse', 'Ingresar'), horizontal=True)

    # Contenedor para la entrada de datos
    with st.container():
        if opcion == 'Registrarse':
            st.subheader('Registro de Nuevo Usuario')
            new_name = st.text_input('Ingresa tu nombre completo para registrarte:')
            new_code = st.text_input('Crea un código de acceso:', type="password")

            if st.button('Registrar'):
                if new_name and new_code:
                    save_user(new_name, new_code)
                else:
                    st.warning("Por favor, ingresa un nombre y un código.")
        
        elif opcion == 'Ingresar':
            st.subheader('Ingresar con tu Cuenta')
            login_name = st.text_input('Ingresa tu nombre de usuario:')
            login_code = st.text_input('Ingresa tu código de acceso:', type="password")
            
            if st.button('Verificar'):
                if login_name and login_code:
                    is_verified, message = verify_user(login_name, login_code)
                    if is_verified:
                        st.success(message)
                    else:
                        st.error(message)
                else:
                    st.warning("Por favor, ingresa tu nombre y código.")

    st.markdown("---")
    st.subheader('Usuarios Registrados')
    # Muestra la lista de usuarios para propósitos de demostración
    if os.path.exists(USUARIOS_FILE):
        df_users = pd.read_csv(USUARIOS_FILE)
        st.dataframe(df_users, use_container_width=True)
    else:
        st.info("Aún no hay usuarios registrados. Usa la pestaña 'Registrarse'.")

if __name__ == "__main__":
    main()
