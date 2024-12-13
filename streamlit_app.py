import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Plataforma de Seguimiento GPS y Registro de Actividades",
    page_icon=":round_pushpin:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
  <div style="display: flex; justify-content: Center; align-items: Center;">
    <img src="https://cdn-icons-png.flaticon.com/128/2118/2118460.png" alt="RRHH YesBpo Logo" width="100" height="100">
    <h1 style='color: #0f0a68; font-size: 29px;'> Plataforma de Seguimiento GPS y Registro de Actividades</h1>
  </div>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: left; color: #0f0a68; font-size: 15px;'>El presente proyecto busca optimizar la gestión de recursos y mejorar la productividad a través de un sistema de geolocalización y registro temporal. Al conocer la ubicación exacta de las personas y equipos en tiempo real, las organizaciones podrán tomar decisiones más informadas, optimizar rutas, reducir costos operativos y mejorar la coordinación de tareas. La plataforma también permitirá generar reportes detallados sobre los movimientos y actividades realizadas, facilitando el análisis de datos y la identificación de patrones.</h1>
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
    zoom=15,  # Zoom al mapa para ver un par de cuadras
    height=600
)

fig.update_layout(mapbox_style="carto-positron")  # Estilo de mapa más sencillo
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)

# Mostrar el DataFrame en Streamlit
st.dataframe(dfDatos)
