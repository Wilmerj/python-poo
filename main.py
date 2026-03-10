from crear_libros import CrearLibros
from biblioteca import Biblioteca
from usuarios import Profesor
from data import data_libros, data_estudiantes
from exceptions import UsuarioNoEncontradoError, LibroNoDisponibleError, TituloInvalidoError

biblioteca = Biblioteca("Biblioteca Central")

profesor = Profesor("Pedro", "1234567890")
biblioteca.usuarios = [profesor, *data_estudiantes]
biblioteca.libros = [*data_libros]

print('Bienvenido a la biblioteca')
print('Libros disponibles:')
for libro in biblioteca.libros:
    print(f'  - {libro.titulo}')
cedula = input("Ingrese la cedula del usuario: ")
usuario = None
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(f'Bienvenido {usuario.nombre}')
except UsuarioNoEncontradoError as e:
    print(e)

titulo = input("Ingrese el titulo del libro: ")
libro = None
try:
    libro = biblioteca.buscar_libro(titulo)
    print(f'Libro encontrado: {libro.titulo}')
except LibroNoDisponibleError as e:
    print(e)

if usuario and libro:
    try:
        resultado = usuario.solicitar_libro(libro.titulo)
        print("\nResultado de la solicitud: ", resultado)
    except TituloInvalidoError as e:
        print(e)

    try:
        resultado_prestar = libro.prestar()
        print("\nResultado de la prestación: ", resultado_prestar)
    except LibroNoDisponibleError as e:
        print(e)
else:
    print("\nNo se encontró el usuario o el libro")