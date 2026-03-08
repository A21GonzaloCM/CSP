from abc import ABC, abstractmethod

# Clase de excepcion personalizada
class RecetaError(Exception):
    """Excepción base para errores en la gestión de recetas."""
    def __init__(self, mensaje="Ha ocurrido un error en la receta"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


# Clases Abstractas
class ElementoNombrado(ABC):
    """Clase abstracta para cualquier cosa que tenga un nombre."""
    
    def __init__(self, nombre):
        
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre
    
    @abstractmethod
    def mostrar_info(self):
        """Método que deben implementar las clases hijas obligatoriamente."""
        pass        

class Imagen:
    def __init__(self, url):
        self.url = url

