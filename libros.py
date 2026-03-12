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
        self._veces_prestado = 0

    @classmethod
    def crear_no_disponible(cls, titulo: str, autor: str, isbn: str):
        return cls(titulo, autor, isbn, disponible=False)

    def __str__(self):
        return f'{self.titulo} - {self.autor} - {self.isbn} - {self.disponible}'

    def prestar(self):
        if not self.disponible:
            raise LibroNoDisponibleError(f"El libro {self.titulo} no está disponible")
        self.disponible = False
        self._veces_prestado += 1
        return f'{self.titulo} prestado'

    def devolver(self):
        self.disponible = True
        return f'{self.titulo} devuelto'

    def calcular_duracion(self) -> str:
        return "Consultar"

    @property
    def es_popular(self):
        return 'es popular' if self._veces_prestado > 5 else 'no es popular'

    @property
    def veces_prestado(self):
        return self._veces_prestado

    @veces_prestado.setter
    def veces_prestado(self, veces_prestado: int):
        if veces_prestado > 0:
            self._veces_prestado = veces_prestado
        else:
            raise ValueError("El numero de veces prestado no puede ser negativo")

    @property
    def descripcion_completa(self):
        return f'{self.titulo} por {self.autor} (ISBN: {self.isbn})'

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