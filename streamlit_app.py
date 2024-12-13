import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar la página de Streamlit
st.set_page_config(
    page_title="Ubicaciones en Bogotá",
    page_icon=":round_pushpin:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
  <div style="display: flex; justify-content: Center; align-items: Center;">
    <img src="https://cdn-icons-png.flaticon.com/128/2118/2118460.png" alt="RRHH YesBpo Logo" width="100" height="100">
    <h1 style='color: #0f0a68; font-size: 29px;'> Proyecto Recursos Humanos</h1>
  </div>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: left; color: #0f0a68; font-size: 15px;'>Transparencia y claridad en cada paso. Conoce el estado de tus solicitudes y mantente informado sobre los procesos de RRHH. ¡Tu tranquilidad es nuestra prioridad!</h1>
    """, unsafe_allow_html=True)

# Cargar los datos desde Google Sheets
gsheetid = '115uUjA9zzHSsfwoSC3mt5VM4E3Abg3jZcQwKQ2zrDzY'
sheetod = '0'
url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetod}&format'

dfDatos = pd.read_csv(url)

# Supongamos que la columna de localización está en el formato "latitud, longitud"
# Separar las coordenadas de latitud y longitud
dfDatos[['Latitud', 'Longitud']] = dfDatos['LOCALIZACION'].str.split(',', expand=True)
dfDatos['Latitud'] = dfDatos['Latitud'].astype(float)
dfDatos['Longitud'] = dfDatos['Longitud'].astype(float)

# Crear el gráfico de mapa con Plotly
fig = px.scatter_mapbox(
    dfDatos, 
    lat="Latitud", 
    lon="Longitud", 
    hover_name="FUNCIONARIO", 
    hover_data=["LOCALIZACION"],
    color="FUNCIONARIO",  # Diferentes colores para diferentes personas
    zoom=12,  # Zoom al mapa para ver más de cerca
    height=600
)

fig.update_layout(mapbox_style="carto-positron")  # Estilo de mapa más sencillo
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)

# Mostrar el DataFrame en Streamlit
st.dataframe(dfDatos)


