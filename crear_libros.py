from libros import Libro
from libros import LibroFisico
from libros import LibroDigital
class CrearLibros:
    def __init__(self):
        self.libros = []

    def crear_libro(self, titulo: str, autor: str, isbn: str, disponible: bool):
        self.libros.append(Libro(titulo, autor, isbn, disponible))

    def crear_libro_fisico(self, titulo: str, autor: str, isbn: str, disponible: bool):
        self.libros.append(LibroFisico(titulo, autor, isbn, disponible))

    def crear_libro_digital(self, titulo: str, autor: str, isbn: str, disponible: bool):
        self.libros.append(LibroDigital(titulo, autor, isbn, disponible))

    def get_libros(self):
        return self.libros