class BibliotecaError(Exception):
    """Excepción base para todas las excepciones de la biblioteca"""
    pass

class TituloInvalidoError(BibliotecaError):
    """Excepción que se lanza cuando el título de un libro es inválido"""
    pass

class LibroNoDisponibleError(BibliotecaError):
    """Excepción que se lanza cuando un libro no está disponible"""
    pass

class UsuarioNoEncontradoError(BibliotecaError):
    """Excepción que se lanza cuando no se encuentra un usuario en la biblioteca"""
    pass