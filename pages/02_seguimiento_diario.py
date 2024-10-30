import streamlit as st
from datetime import date

from src.util.HabitosException import HabitosExcepcion


def seguimiento_diario(controlador):
    st.title("Seguimiento Diario de Hábitos")

    # Seleccionar un hábito y registrar seguimiento
    habito_dict = {habito.nombre: habito.id for habito in controlador.obtener_habitos()}
    habit_nombre = st.selectbox("Selecciona un hábito para administrar", options=list(habito_dict.keys()))
    habit_id = habito_dict.get(habit_nombre)
    fecha = st.date_input("Fecha", date.today())
    completado = st.checkbox("Cumplido")

    if st.button("Registrar Seguimiento"):
        try:
            controlador.registrar_habito(fecha, habit_id, completado)
            st.success("Seguimiento registrado correctamente.")
        except HabitosExcepcion as e:
            st.error(str(e))
        except Exception as e:
            st.error("Error contacte a administrador.")
            # FIXME
            # Agregar el error en un archivo de log
        st.sidebar.markdown("### Botón oprimido 🎈")

# Ejecutar la función en la página
seguimiento_diario(st.session_state.controlador)