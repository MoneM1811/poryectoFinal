# Importar librerías
import streamlit as st
import joblib  # ✅ Ahora usamos joblib, no pickle
import numpy as np
 
# Cargar el modelo correctamente
model = joblib.load("mejor_modelo_precio.pkl")  # ✅ Correcto: carga con joblib
 
# Configuración de la página
st.set_page_config(page_title="Predicción de Precios de Casas", page_icon="🏠", layout="wide")
 
# Menú lateral
st.sidebar.title("HAZ TU SELECCIÓN:")
page = st.sidebar.radio("Ir a", ("Inicio", "Predicción"))
 
# Página de inicio
if page == "Inicio":
    # Imagen de bienvenida (asegúrate que 'imagen.jpg' esté en la misma carpeta o comenta esta línea si no tienes imagen)
    st.image("imagen.jpg", caption="¡Bienvenidos a la Predicción de Precios de Casas!", width=700)
    # Título
    st.title("Predicción de Precios de Casas")
 
    # Texto explicativo
    st.markdown("""
        Este modelo predice el precio de casas basándose en características como el promedio de habitaciones, 
        la proporción de terrenos residenciales y otros factores.
    """)
 
    # Integrantes del grupo
    st.markdown("### Integrantes del grupo:")
    st.markdown("- **1) Jenny Villacis**")
    st.markdown("- **2) Nathaly Aguilar**")
    st.markdown("- **3) Oswaldo Sotomayor**")
 
    # Enlaces externos
    st.markdown("### Revisa el modelo y el código:")
    st.markdown("[Revisa el modelo en Colab:](https://colab.research.google.com/drive/1bF7ueCsLVuk0PxUUWaprldVMsftJJvBW?usp=sharing)")
    st.markdown("[Revisa el código en GitHub:](https://github.com/oswaldosotomayor/poryectoFinal.git)")
 
# Página de predicción
elif page == "Predicción":
    st.title("¡Haz tu Predicción de Precios de Casas!")
 
    # Entradas del usuario
    RM = st.number_input('Promedio de habitaciones por vivienda:', value=6.0)
    ZN = st.number_input('Proporción de terrenos residenciales de más de 25,000 pies cuadrados:', value=0.0)
    PTRATIO = st.number_input('Proporción de alumnos por maestro:', value=18.0)
    LSTAT = st.number_input('Porcentaje de población de bajo estatus socioeconómico:', value=12.0)
 
    # Botón para hacer la predicción
    if st.button('Predecir Precio'):
        # Crear el arreglo de entrada
        input_data = np.array([[RM, ZN, PTRATIO, LSTAT]])
 
        # Hacer la predicción
        prediction = model.predict(input_data)
 
        # ✅ Acceder de forma segura al resultado
        resultado = f'${float(prediction[0])*1000:,.2f}'  # Formato en miles de dólares
 
        # Mostrar el resultado bonito
        st.markdown(f"""
<div style="background-color:#f2f2f2; padding: 20px; border-radius: 10px; border: 3px solid #4CAF50; text-align:center; font-size: 40px; color: #4CAF50;">
<b>El precio estimado de la casa es:</b> <span style="color:#D32F2F; font-size: 45px; font-weight: bold;">{resultado}</span>
</div>
        """, unsafe_allow_html=True)
 
    # Explicación adicional
    st.markdown("""
    ### ¿Cómo funciona esta predicción?
    Este modelo utiliza variables como el promedio de habitaciones, la proporción de terrenos residenciales 
    y la proporción de alumnos por maestro para predecir el precio de una vivienda.
 
    Es ideal para tener una idea aproximada del precio de una casa en base a características específicas de la propiedad.
    """)