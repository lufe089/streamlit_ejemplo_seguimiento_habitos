import streamlit as st

import streamlit as st
import pandas as pd

from src.util.HabitosException import HabitosExcepcion


def mostrar_habitos(controlador):
    """
    Muestra una lista de hábitos en un DataFrame con opciones para editar, cambiar de estado y eliminar cada hábito.

    Parámetros:
    -----------
    controlador : ControladorHabitos
        Instancia del controlador que maneja la lógica de los hábitos.
    """

    # Crear una lista de diccionarios con los datos de cada hábito para visualización
    habitos_data = []
    for habito_id, habito in controlador._habitos.items():
        habitos_data.append({
            "ID": habito.id,
            "Nombre": habito.nombre,
            "Descripción": habito.descripcion,
            "Estado": "Activo" if habito.is_activo() else "Inactivo"
        })

    # Convertir los datos a un DataFrame de pandas
    df_habitos = pd.DataFrame(habitos_data)

    # Mostrar el DataFrame de los hábitos
    st.write("Lista de Hábitos:")
    st.write(df_habitos)

    # Agregar botones para cada hábito
    for index, row in df_habitos.iterrows():
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])  # Definir columnas para los botones
        with col1:
            st.write(f"{row['Nombre']}")
        with col2:
            # Botón de Editar
            if st.button("Editar", key=f"edit_{row['ID']}"):
                editar_habito(controlador, row['ID'])
        with col3:
            # Botón de Cambiar Estado
            if st.button("Cambiar Estado", key=f"toggle_{row['ID']}"):
                cambiar_estado_habito(controlador, row['ID'])
        with col4:
            # Botón de Eliminar
            if st.button("Eliminar", key=f"delete_{row['ID']}"):
                eliminar_habito(controlador, row['ID'])


def editar_habito(controlador, habito_id):
    """
    Función para editar un hábito específico.

    Parámetros:
    -----------
    controlador : ControladorHabitos
        Instancia del controlador que maneja la lógica de los hábitos.
    habito_id : int
        ID del hábito que se quiere editar.
    """
    habito = controlador.obtener_habito(habito_id)
    if habito:
        nombre = st.text_input("Editar Nombre del Hábito", value=habito.nombre)
        descripcion = st.text_area("Editar Descripción", value=habito.descripcion)
        if st.button("Guardar Cambios", key=f"save_{habito_id}"):
            habito.nombre = nombre
            habito.descripcion = descripcion
            st.success(f"Hábito '{nombre}' actualizado correctamente.")


def cambiar_estado_habito(controlador, habito_id):
    """
    Función para cambiar el estado de un hábito.

    Parámetros:
    -----------
    controlador : ControladorHabitos
        Instancia del controlador que maneja la lógica de los hábitos.
    habito_id : int
        ID del hábito que se quiere cambiar de estado.
    """
    habito = controlador.obtener_habito(habito_id)
    if habito:
        habito.desactivar() if habito.is_activo() else habito.activar()
        nuevo_estado = "Activo" if habito.is_activo() else "Inactivo"
        st.success(f"El estado del hábito '{habito.nombre}' ha sido cambiado a {nuevo_estado}.")


def eliminar_habito(controlador, habito_id):
    """
    Función para eliminar un hábito.

    Parámetros:
    -----------
    controlador : ControladorHabitos
        Instancia del controlador que maneja la lógica de los hábitos.
    habito_id : int
        ID del hábito que se quiere eliminar.
    """
    try:
        controlador.eliminar_habito(habito_id)
        st.success(f"Hábito con ID {habito_id} eliminado correctamente.")
    except HabitosExcepcion as e:
        st.error(str(e))


def probar_streamlit():
    """ Ponga aqui todos los controles de prueba para que entienda como funciona"""
    st.write("Agregue aquí botones, paneles, y opciones tal como se describe en el readme")
    st.button("Soy un boton")


# Main call
if __name__ == "__main__":
    mostrar_habitos(st.session_state.controlador)