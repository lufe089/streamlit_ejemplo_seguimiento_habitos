"""
Punto de entrada del programa
"""
from src.model.ControladorHabitos import ControladorHabitos

import streamlit as st

def iniciar_programa():
    # Asigna el controlador como variable de instancia y en session_state para persistencia
    if 'controlador' not in st.session_state:
        st.session_state.controlador = ControladorHabitos()

    # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
    st.set_page_config(page_title="Aplicación de Gestión de Hábitos", page_icon="🕹️", layout="wide",
                       initial_sidebar_state="expanded")
    st.write("Usa el menú de la barra lateral para navegar entre las secciones de la aplicación.")


if __name__ == "__main__":
    iniciar_programa()


