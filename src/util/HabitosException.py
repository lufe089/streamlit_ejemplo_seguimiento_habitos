class HabitosExcepcion(Exception):
    """
    Excepción base para todas las excepciones relacionadas con los hábitos.
    """
    def __init__(self, message = "Ha ocurrido un error relacionado con los hábitos."):
        self.message = message
        super().__init__(self.message)