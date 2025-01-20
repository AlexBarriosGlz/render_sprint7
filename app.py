import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Vehículos US')
car_data = pd.read_csv('\notebook\vehicles_us.csv')
hist_button = st.button('Construir histograma') 

if hist_button: 
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

if disp_button: 
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    fig = px.scatter(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

streamlit run app.py