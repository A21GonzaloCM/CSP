from .plato import Plato
from .base import RecetaError

class Gestor:
    def __init__(self):
        self._catalogo_platos = []

    def crear_plato(self, nombre, tiempo):
        # Uso del método estático antes de crear
        if not Plato.validar_tiempo(tiempo):
            raise RecetaError("Tiempo de preparación inválido")
        
        nuevo_plato = Plato(nombre, tiempo)
        self._catalogo_platos.append(nuevo_plato)
        print(f"Plato '{nombre}' creado con éxito.")
        return nuevo_plato

    def buscar_por_nombre(self, nombre):
        for plato in self._catalogo_platos:
            if plato.nombre.lower() == nombre.lower():
                return plato
        return None