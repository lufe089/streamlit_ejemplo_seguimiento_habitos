import streamlit as st

def exportar_datos(controlador):
    page_title = "Exportar Datos de Hábitos"
    st.title(page_title)
    st.sidebar.markdown(f"# {page_title} 🎈")

    nombre_archivo = st.text_input("Nombre del archivo", value="habitos_exportados")
    if st.button("Exportar a Excel"):
        controlador.exportar_habitos(nombre_archivo)
        st.success(f"Datos exportados exitosamente a '{nombre_archivo}.xlsx'")

# Ejecutar la función en la página
exportar_datos(st.session_state.controlador)