from typing import Protocol

class LibroProtocol(Protocol):
    def prestar(self) -> str:
        """Metodo que debe implementar cualquier clase que implemente este protocolo"""
        ...
    def calcular_duracion(self) -> str:
        """Metodo que debe implementar cualquier clase que implemente este protocolo"""
        ...

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.prestamos = 0

    def __str__(self):
        return f'{self.titulo} - {self.autor} - {self.isbn} - {self.disponible}'

    def prestar(self):
        self.disponible = False
        self.prestamos += 1
        return f'{self.titulo} prestado'
    
    def devolver(self):
        self.disponible = True
        return f'{self.titulo} devuelto'

    def es_popular(self):
        return 'es popular' if self.prestamos > 4 else 'no es popular'

class LibroFisico(Libro):
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool):
        super().__init__(titulo, autor, isbn, disponible)
        self.paginas = 100

    def calcular_duracion(self):
        return f'{self.titulo} tiene {self.paginas} paginas'

class LibroDigital(Libro):
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool):
        super().__init__(titulo, autor, isbn, disponible)
        self.tamanio = 100

    def calcular_duracion(self):
        return f'{self.titulo} tiene {self.tamanio} MB'

mi_libro = Libro("El principito", "Antoine de Saint-Exupéry", "1234567890", True)
print(mi_libro.prestar())
print(mi_libro.prestar())
print(mi_libro.prestar())
print(mi_libro.prestar())
print(mi_libro.prestar())
print(mi_libro.es_popular())

otro_libro = Libro("1984", "George Orwell", "1234567890", True)
libro_fisico = LibroFisico("El principito", "Antoine de Saint-Exupéry", "1234567890", True)
libro_digital = LibroDigital("1984", "George Orwell", "1234567890", True)

catalogo: list[Libro] = [mi_libro, otro_libro]
catalogo_libros: list[LibroProtocol] = [libro_fisico, libro_digital]

for libro in catalogo:
    print(f'libro: {libro}')