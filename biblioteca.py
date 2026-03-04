from libros import Libro

class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros: list[Libro] = []

    def libros_disponibles(self):
        return [str(libro) for libro in self.libros if libro.disponible]