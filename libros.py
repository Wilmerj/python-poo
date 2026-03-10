from typing import Protocol
from abc import ABC, abstractmethod
from exceptions import LibroNoDisponibleError
class LibroProtocol(Protocol):
    def prestar(self) -> str:
        """Metodo que debe implementar cualquier clase que implemente este protocolo"""
        ...
    def devolver(self) -> str:
        """Metodo que debe implementar cualquier clase que implemente este protocolo"""
        ...
    def calcular_duracion(self) -> str:
        """Metodo que debe implementar cualquier clase que implemente este protocolo"""
        ...

class LibroBase(ABC):
    @abstractmethod
    def prestar(self) -> str:
        pass
    @abstractmethod
    def devolver(self) -> str:
        pass
    @abstractmethod
    def calcular_duracion(self) -> str:
        pass
    @abstractmethod
    def es_popular(self) -> str:
        pass
class Libro(LibroBase):
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.prestamos = 0

    def __str__(self):
        return f'{self.titulo} - {self.autor} - {self.isbn} - {self.disponible}'

    def prestar(self):
        if not self.disponible:
            raise LibroNoDisponibleError(f"El libro {self.titulo} no está disponible")
        self.disponible = False
        self.prestamos += 1
        return f'{self.titulo} prestado'

    def devolver(self):
        self.disponible = True
        return f'{self.titulo} devuelto'

    def es_popular(self):
        return 'es popular' if self.prestamos > 4 else 'no es popular'

class LibroFisico(Libro):
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True):
        super().__init__(titulo, autor, isbn, disponible)
        self.paginas = 100

    def calcular_duracion(self):
        return f'7 dias'

class LibroDigital(Libro):
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True):
        super().__init__(titulo, autor, isbn, disponible)
        self.tamanio = 100

    def calcular_duracion(self):
        return f'14 dia'