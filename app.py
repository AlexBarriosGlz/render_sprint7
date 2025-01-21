import pandas as pd 
import plotly.express as px
import streamlit as st


car_data = pd.read_csv('vehicles_us.csv')
st.header('Vehículos US')

hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir un gráfico de dispersión')

st.header('Análisis de vehículos usados en US')

if hist_button: 
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_button: 
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y ="price", title="Odómetro vs Precio")
    st.plotly_chart(fig, use_container_width=True)

