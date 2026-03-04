from libros import Libro, LibroFisico, LibroDigital
from biblioteca import Biblioteca
from usuarios import Estudiante, Profesor, SolicitanteProtocol
from exceptions import BibliotecaError, LibroNoDisponibleError

mi_libro = Libro("El principito", "Antoine de Saint-Exupéry", "1234567890", True)
otro_libro = Libro("1984", "George Orwell", "1234567890", False)
libro_fisico = LibroFisico("El principito", "Antoine de Saint-Exupéry", "1234567890", False)
libro_digital = LibroDigital("1984", "George Orwell", "1234567890", True)

biblioteca = Biblioteca("Biblioteca Central")
biblioteca.libros = [mi_libro, otro_libro, libro_fisico, libro_digital]

print(biblioteca.libros_disponibles())

estudiante = Estudiante("Juan", "1234567890", "Ingeniería")
profesor = Profesor("Pedro", "1234567890")

from main import Libro
libro = Libro("El principito", "Antoine de Saint-Exupéry", "1234567890", True)

usuarios: list[SolicitanteProtocol] = [estudiante, profesor]

for usuario in usuarios:
    print(usuario.solicitar_libro(libro.titulo))

try:
    resultado = estudiante.solicitar_libro(None)
except BibliotecaError as e:
    print(e)

try:
    resultado = Libro("El principito", "Antoine de Saint-Exupéry", "1234567890", False).prestar()
except LibroNoDisponibleError as e:
    print(e)

resultado2 = estudiante.solicitar_libro("El principito")
print(resultado2)