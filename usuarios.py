from typing import Protocol

class SolicitanteProtocol(Protocol):
    def solicitar_libro(self, titulo: str) -> str:
        """Metodo que debe implementar cualquier clase que implemente este protocolo"""
        ...
class Usuario:
    def __init__(self, nombre: str, cedula: str):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados: list[str] = []

    def solicitar_libro(self, titulo: str):
        return f"Solicitud del libro {titulo} realizada"

class Estudiante(Usuario):
    def __init__(self, nombre: str, cedula: str, carrera: str):
        super().__init__(nombre, cedula)
        self.carrera = carrera
        self.limite_libros = 3

    def solicitar_libro(self, titulo: str):
        if len(self.libros_prestados) < self.limite_libros:
            self.libros_prestados.append(titulo)
            return f"Solicitud del libro {titulo} realizada"
        else:
            return f"No se puede solicitar el libro {titulo} porque se ha alcanzado el límite de libros prestados"

    def devolver_libro(self, titulo: str):
        if titulo in self.libros_prestados:
            self.libros_prestados.remove(titulo)
            return f"Libro {titulo} devuelto"
        else:
            return f"El libro {titulo} no está prestado"


class Profesor(Usuario):
    def __init__(self, nombre: str, cedula: str):
        super().__init__(nombre, cedula)
        self.limite_libros = None

    def solicitar_libro(self, titulo: str):
        self.libros_prestados.append(titulo)
        return f"Solicitud del libro {titulo} realizada"
