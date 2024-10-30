class RegistroHabito:
    """
    Clase que representa un registro diario de cumplimiento de un hábito.

    Atributos:
    ----------
    fecha : date
        Fecha del registro.
    habito : Habito
        Instancia del hábito al que se refiere el registro.
    completado : bool
        Estado de cumplimiento del hábito en la fecha dada.
    """

    def __init__(self, fecha, habito, completado=False):
        self._fecha = fecha
        self._habito = habito
        self._completado = completado

    def esta_completado(self):
        """
        Verifica si el hábito fue completado en la fecha del registro.

        Retorna:
        --------
        bool
            True si el hábito fue completado, False en caso contrario.
        """
        return self._completado