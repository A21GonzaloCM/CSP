from datetime import date
from .base import ElementoNombrado
from .ingrediente import Ingrediente
from .base import RecetaError
from .base import Imagen

class Plato(ElementoNombrado):
    def __init__(self, nombre, tiempo_prep, es_comida=True):
        super().__init__(nombre)
        self._ingredientes = []  
        self._pasos = []       
        self.tiempo_prep = tiempo_prep
        self.fecha_creacion = date.today()
        self.es_comida = es_comida
        self.imagen = None       

    def agregar_ingrediente(self, ingrediente):

        if isinstance(ingrediente, Ingrediente):
            self._ingredientes.append(ingrediente)
        else:
            raise RecetaError("El objeto no es un ingrediente válido")

    def asignar_imagen(self, url):
        self.imagen = Imagen(url)

    def mostrar_info(self):
        tipo = "Comida" if self.es_comida else "Bebida"
        return f"{self.nombre} ({tipo}) - {self.tiempo_prep} min."

    def __len__(self):
        return len(self._ingredientes)

    @staticmethod
    def validar_tiempo(tiempo):
        """Método estático para validar reglas de negocio sin instanciar."""
        return tiempo > 0 and tiempo < 500        
    

# Outro caso de herdanza
class PlatoGourmet(Plato):
    def __init__(self, nombre, tiempo_prep, chef_autor):
        super().__init__(nombre, tiempo_prep)
        self.chef_autor = chef_autor

    def mostrar_info(self):
        base = super().mostrar_info()
        return f"{base} - Creado por Chef: {self.chef_autor}"
    