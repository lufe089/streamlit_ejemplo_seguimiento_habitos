import streamlit as st

st.write("hola mundo")
seleccionado = st.button("Soy un boton")
col1, col2 = st.columns([3,1])
if seleccionado:
    st.write("Me has seleccionado")
    col1.write("Soy la columna 1")
    col2.write("Soy la columna 2")