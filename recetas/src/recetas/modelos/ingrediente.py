from .base import ElementoNombrado
from .base import RecetaError

class Ingrediente(ElementoNombrado):
    def __init__(self, nombre, cantidad, unidad_medida):
        super().__init__(nombre)
        self._cantidad = cantidad
        self._unidad_medida = unidad_medida

    def __str__(self):
        return f"{self._cantidad} {self._unidad_medida} de {self.nombre}"

    def __eq__(self, otro):
        if isinstance(otro, Ingrediente):
            return self.nombre.lower() == otro.nombre.lower()
        return False

    def mostrar_info(self):
        """Implementación obligatoria del método abstracto."""
        return f"Ingrediente: {self.nombre} ({self._cantidad} {self._unidad_medida})"

    def editar_cantidad(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise RecetaError("La cantidad no puede ser negativa")
        self._cantidad = nueva_cantidad