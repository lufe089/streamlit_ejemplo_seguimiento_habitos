class Habito:
    """
    Clase que representa un hábito.

    Atributos:
    ----------
    _id : int
        Identificador único del hábito.
    _nombre : str
        Nombre del hábito.
    _descripcion : str
        Descripción detallada del hábito.
    _categoria : str
        Categoría del hábito (ej., Salud, Productividad, etc.).
    """

    def __init__(self, id, nombre, descripcion, categoria):
        self._id = id
        self.nombre = nombre  # Usamos property para nombre
        self._descripcion = descripcion
        self._categoria = categoria
        self._activo = True

    @property
    def id(self):
        """Devuelve el identificador único del hábito."""
        return self._id

    @property
    def nombre(self):
        """Devuelve el nombre del hábito."""
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """Actualiza el nombre del hábito."""
        min_length = 3
        if len(nuevo_nombre) < min_length:
            raise ValueError("El nombre del hábito debe tener al menos 3 caracteres.")
        self._nombre = nuevo_nombre

    @property
    def categoria(self):
        """Devuelve la categoría del hábito."""
        return self._categoria

    @property
    def descripcion(self):
        """Devuelve la descripción del hábito."""
        return self._descripcion
    def desactivar(self):
        """
        Desactiva el hábito, evitando que se registren nuevos cumplimientos.
        """
        self._activo = False

    def is_activo(self):
        """
        Verifica si el hábito está activo.

        Retorna:
        --------
        bool
            True si el hábito está activo, False en caso contrario.
        """
        return self._activo