from crear_libros import CrearLibros
from biblioteca import Biblioteca
from usuarios import Estudiante, Profesor
from exceptions import UsuarioNoEncontradoError

biblioteca = Biblioteca("Biblioteca Central")
crear_libros = CrearLibros()
crear_libros.crear_libro_fisico("El principito", "Antoine de Saint-Exupéry", "1234567890", True)
crear_libros.crear_libro_digital("100 años de soledad", "Gabriel García Márquez", "1234567890", False)

estudiante = Estudiante("Juan", "1234567890", "Ingeniería")
estudiante_1 = Estudiante("Juan 1", "1234567890", "Ingeniería")
profesor = Profesor("Pedro", "1234567890")

biblioteca.usuarios = [estudiante, estudiante_1, profesor]

print('Bienvenido a la biblioteca')
print('Libros disponibles:')
for libro in crear_libros.get_libros():
    print(f'  - {libro.titulo}')
cedula = input("Ingrese la cedula del usuario: ")
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(f'Bienvenido {usuario.nombre}')
except UsuarioNoEncontradoError as e:
    print(e)