from libros import Libro
from usuarios import Usuario
from exceptions import UsuarioNoEncontradoError, LibroNoDisponibleError
class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros: list[Libro] = []
        self.usuarios: list[Usuario] = []

    def libros_disponibles(self):
        return [str(libro) for libro in self.libros if libro.disponible]

    def buscar_usuario(self, cedula: str):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
        raise UsuarioNoEncontradoError(f"Usuario con cedula {cedula} no encontrado")

    def buscar_libro(self, titulo: str):
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                return libro
        raise LibroNoDisponibleError(f"Libro con titulo {titulo} no disponible")