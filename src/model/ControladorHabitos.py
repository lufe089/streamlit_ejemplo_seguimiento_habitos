
import pandas as pd
from datetime import date

from src.model.Habito import Habito
from src.model.RegistroHabito import RegistroHabito
from src.util.HabitosException import HabitosExcepcion


class ControladorHabitos:
    """
       Clase que gestiona los hábitos, su seguimiento y generación de reportes.

       Atributos:
       ----------
       _habitos : dict
           Diccionario que almacena los hábitos por su ID.
       _registros_habito : dict
           Diccionario donde la clave es una tupla (id de hábito, fecha) y el valor es un RegistroHabito.
       """

    def __init__(self):
        """
        Inicializa un nuevo seguimiento de hábitos.
        """
        self._habitos = {}
        self._contador_habitos = 1
        # Crear cinco habitos iniciales
        self.agregar_habito("Leer 30 minutos", "Leer un libro por 30 minutos al día", "Crecimiento personal")
        self.agregar_habito("Hacer ejercicio", "Realizar 30 minutos de ejercicio cardiovascular", "Salud")
        self.agregar_habito("Meditar", "Meditar 10 minutos al día", "Crecimiento personal")
        self.agregar_habito("Llamar a un amigo", "Llamar a un amigo para mantener el contacto", "Social")
        self.agregar_habito("Limpiar la casa", "Realizar una limpieza general de la casa", "Hogar")
        self._registros_habito = {}


    def agregar_habito(self, nombre, descripcion, categoria):
        """
        Agrega un nuevo hábito al sistema.

        Parámetros:
        -----------
        habito : Habito
            Instancia del hábito a agregar.
        """
        nuevo_habito = Habito(self._contador_habitos,nombre,descripcion,categoria)
        self._habitos[nuevo_habito.id] = nuevo_habito
        # Aumenta el contador de habitos porque esto permite controlar la llave de los habitos
        self._contador_habitos = self._contador_habitos + 1

    def obtener_habito(self, id):
        """
        Obtiene un hábito por su ID.

        Parámetros:
        -----------
        id : int
            ID del hábito a buscar.

        Retorna:
        --------
        Habito
            El hábito correspondiente al ID, o None si no se encuentra.
        """
        return self._habitos.get(id)

    def desactivar_habito(self, id):
        """
        Desactiva un hábito específico por su ID.

        Parámetros:
        -----------
        id : int
            ID del hábito a desactivar.
        """
        habito = self.obtener_habito(id)
        if habito:
            habito.desactivar()
        else:
            raise HabitosExcepcion(f"Hábito con ID {id} no encontrado.")

    def registrar_habito(self, fecha, habito_id, completado):
        """
        Registra el cumplimiento de un hábito en una fecha específica.

        Parámetros:
        -----------
        fecha : date
            Fecha en la que se registra el cumplimiento.
        habito_id : int
            ID del hábito a registrar.
        completado : bool
            Estado de cumplimiento (True si se completó, False si no).

        Excepciones:
        ------------
        HabitosExcepcion:
            Se lanza si el hábito está inactivo.
        """
        habito = self.obtener_habito(habito_id)
        if habito:
            if habito.is_activo():
                registro = RegistroHabito(fecha, habito, completado)
                self._registros_habito[(habito_id, fecha)] = registro
            else:
                raise HabitosExcepcion(
                    f"El hábito '{habito.nombre}' está inactivo y no se puede registrar su cumplimiento.")
        else:
            raise HabitosExcepcion(f"Hábito con ID {habito_id} no encontrado.")

    def obtener_registro(self, habito_id, fecha):
        """
        Obtiene el registro de cumplimiento de un hábito en una fecha específica.

        Parámetros:
        -----------
        habito_id : int
            ID del hábito a buscar.
        fecha : date
            Fecha del registro solicitado.

        Retorna:
        --------
        RegistroHabito
            El registro de cumplimiento en la fecha especificada, o None si no existe.
        """
        return self._registros_habito.get((habito_id, fecha))

    def eliminar_habito(self, habito_id):
        """
        Elimina un hábito si no tiene registros de cumplimiento asociados.

        Parámetros:
        -----------
        habito_id : int
            ID del hábito a eliminar.

        Excepciones:
        ------------
        HabitosExcepcion:
            Se lanza si el hábito tiene registros de cumplimiento y no puede ser eliminado.
        """
        for registro_key in self._registros_habito:
            if registro_key[0] == habito_id:
                raise HabitosExcepcion(
                    f"No se puede eliminar el hábito con ID {habito_id} porque tiene registros de cumplimiento.")

        if habito_id in self._habitos:
            del self._habitos[habito_id]
        else:
            raise HabitosExcepcion(f"Hábito con ID {habito_id} no encontrado.")

    def generar_reporte_cumplimiento(self, fecha_inicio, fecha_fin):
        """
        Genera un reporte de cumplimiento de los hábitos en un periodo de tiempo específico.

        Parámetros:
        -----------
        fecha_inicio : date
            Fecha de inicio del reporte.
        fecha_fin : date
            Fecha de fin del reporte.

        Retorna:
        --------
        DataFrame
            DataFrame que contiene el porcentaje de cumplimiento de cada hábito en el periodo especificado.
        """
        reporte_data = []

        for habito_id, habito in self._habitos.items():
            registros_cumplidos = 0
            total_registros = 0

            for (id_h, fecha), registro in self._registros_habito.items():
                if id_h == habito_id and fecha_inicio <= fecha <= fecha_fin:
                    total_registros += 1
                    if registro.esta_completado():
                        registros_cumplidos += 1

            if total_registros > 0:
                porcentaje_cumplimiento = (registros_cumplidos / total_registros) * 100
            else:
                porcentaje_cumplimiento = 0.0

            reporte_data.append({
                'Hábito': habito.nombre,
                'Porcentaje Cumplimiento (%)': porcentaje_cumplimiento
            })

        df_reporte = pd.DataFrame(reporte_data)
        return df_reporte

    def exportar_habitos(self, nombre_archivo):
        """
        Exporta los hábitos y sus registros de cumplimiento a un archivo Excel.

        Parámetros:
        -----------
        nombre_archivo : str
            Nombre del archivo Excel al cual se exportarán los datos.
        """
        datos = []
        for habito_id, habito in self._habitos.items():
            for (id_h, fecha), registro in self._registros_habito.items():
                if id_h == habito_id:
                    datos.append({
                        'ID Hábito': habito.id,
                        'Nombre': habito.nombre,
                        'Descripción': habito._descripcion,
                        'Categoría': habito.categoria,
                        'Activo': habito.is_activo(),
                        'Fecha': fecha,
                        'Cumplido': registro.esta_completado()
                    })

        df = pd.DataFrame(datos)
        nombre_archivo = f"{nombre_archivo}.xlsx" if not nombre_archivo.endswith('.xlsx') else nombre_archivo
        df.to_excel(nombre_archivo, index=False)
        return f"Datos exportados exitosamente a {nombre_archivo}"

    def consultar_contador_habitos (self):
        return self._contador_habitos

    def obtener_habitos(self):
        """
        Obtiene una lista de todos los habitos registrados
        """
        return self._habitos.values()