import streamlit as st
import pickle
import numpy as np

# Cargar el modelo
model = pickle.load(open("precios.pkl", "rb"))

# Título de la aplicación
st.title("Predicción de Precios de Casas")

# Entradas de las variables en el orden correcto
RM = st.number_input('Promedio de habitaciones por vivienda (RM)', value=6.0)
ZN = st.number_input('Proporción de terrenos residenciales de más de 25,000 pies cuadrados (ZN)', value=0.0)
PTRATIO = st.number_input('Proporción de alumnos por maestro (PTRATIO)', value=18.0)
LSTAT = st.number_input('Porcentaje de población de bajo estatus socioeconómico (LSTAT)', value=12.0)

# Botón para hacer la predicción
if st.button('Predecir Precio'):
    # Crear el arreglo de entrada con el orden correcto
    input_data = np.array([[RM, ZN, PTRATIO, LSTAT]])

    # Hacer la predicción
    prediction = model.predict(input_data)

    # Acceder al valor de la predicción y mostrarla
    st.write(f'El precio estimado de la casa es: ${prediction[0][0]:,.2f}')
