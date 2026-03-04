class BibliotecaError(Exception):
    pass

class TituloInvalidoError(BibliotecaError):
    pass

class LibroNoDisponibleError(BibliotecaError):
    pass