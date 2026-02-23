class Usuario:
    def __init__(self, nombre: str, cedula: str):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

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


class Profesor(Usuario):
    def __init__(self, nombre: str, cedula: str):
        super().__init__(nombre, cedula)
        self.limite_libros = None

    def solicitar_libro(self, titulo: str):
        self.libros_prestados.append(titulo)
        return f"Solicitud del libro {titulo} realizada"


estudiante = Estudiante("Juan", "1234567890", "Ingeniería")
profesor = Profesor("Pedro", "1234567890")

print(estudiante.solicitar_libro("El principito"))
print(estudiante.solicitar_libro("El principito"))
print(estudiante.solicitar_libro("El principito"))
print(estudiante.solicitar_libro("El principito"))
print(profesor.solicitar_libro("El asesinato del总统"))