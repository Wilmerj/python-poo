from crear_libros import CrearLibros
from exceptions import UsuarioNoEncontradoError, LibroNoDisponibleError, TituloInvalidoError
from persistencia import Persistencia
from data import data_libros, data_estudiantes
from usuarios import Profesor

persistencia = Persistencia()
biblioteca = persistencia.cargar_datos()

# Si el JSON estaba vacío, cargar datos iniciales y guardar para la próxima
if not biblioteca.libros and not biblioteca.usuarios:
    biblioteca.libros = [*data_libros]
    biblioteca.usuarios = [Profesor("Pedro", "1234567890"), *data_estudiantes]
    persistencia.guardar_datos(biblioteca)
# libro_no_disponible = Libro.crear_no_disponible("50 años de soledad no disponible", "Gabriel García Márquez", "1234567890")
# print(libro_no_disponible.disponible)

# estudiante_software = Estudiante.crear_estudiante_software("Juan", "1234567890")
# print(estudiante_software.carrera)

print('Bienvenido a la biblioteca')
print('Libros disponibles:')
for libro in biblioteca.libros_disponibles:
    print(f'  - {libro.descripcion_completa}')

print('Usuarios:')
for usuario in biblioteca.usuarios:
    print(f'  - {usuario.nombre_completo}')

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
        libro.veces_prestado += 1
        print("\nResultado de la prestación: ", resultado_prestar)
        print(f"El libro {libro.titulo} ha sido prestado {libro.veces_prestado} veces")
    except LibroNoDisponibleError as e:
        print(e)
else:
    print("\nNo se encontró el usuario o el libro")

# resultado = Biblioteca.validar_isbn("1221320")
# print(f"El ISBN es valido: {resultado}")