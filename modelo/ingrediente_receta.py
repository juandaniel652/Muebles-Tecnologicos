# modelo/ingrediente_receta.py

class IngredienteReceta :

    def __init__ (self, nombre: str, cantidad: float, unidad: str) :

        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad = unidad

    def __str__ (self) :
        
        return f"{self.cantidad} {self.unidad} de {self.nombre}"
