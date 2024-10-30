import streamlit as st

def gestion_habitos(controlador):
    st.title("Gestión de Hábitos")

    # Agregar un nuevo hábito
    st.subheader("Agregar un nuevo hábito")
    nombre = st.text_input("Nombre del hábito")
    descripcion = st.text_area("Descripción")
    categoria = st.selectbox("Categoría", ["Salud", "Productividad", "Crecimiento personal", "Social", "Hogar"])

    if st.button("Agregar Hábito"):
        if nombre:
            controlador.agregar_habito(nombre, descripcion, categoria)
            st.success(f"Hábito '{nombre}' agregado correctamente.")
        else:
            st.error("El nombre del hábito es obligatorio.")

    # Selección de hábito para administrar

    # Obtener un diccionario con los hábitos activos a partir de los nombres
    habito_dict = {habito.nombre: habito.id for habito in controlador.obtener_habitos()}
    habit_nombre = st.selectbox("Selecciona un hábito para administrar", options=list(habito_dict.keys()))
    habit_id = habito_dict.get(habit_nombre)

    # Desactivar o eliminar un hábito
    if habit_id:
        habito = controlador.obtener_habito(habit_id)
        if habito:
            if st.button("Desactivar Hábito"):
                controlador.desactivar_habito(habit_id)
                st.success(f"Hábito '{habito.nombre}' desactivado correctamente.")
            if st.button("Eliminar Hábito"):
                controlador.eliminar_habito(habit_id)
                st.success(f"Hábito '{habito.nombre}' eliminado correctamente.")

# Ejecutar la función en la página
gestion_habitos(st.session_state.controlador)