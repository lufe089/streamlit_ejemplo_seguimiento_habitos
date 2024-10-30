import streamlit as st

def reporte_cumplimiento(controlador):
    st.title("Reporte de Cumplimiento de Hábitos")

    fecha_inicio = st.date_input("Fecha de inicio")
    fecha_fin = st.date_input("Fecha de fin")

    if st.button("Generar Reporte"):
        if fecha_inicio <= fecha_fin:
            reporte = controlador.generar_reporte(fecha_inicio, fecha_fin)
            st.write("Reporte de Cumplimiento:")
            st.dataframe(reporte)
        else:
            st.error("La fecha de inicio debe ser anterior a la fecha de fin.")

# Ejecutar la función en la página
reporte_cumplimiento(st.session_state.controlador)