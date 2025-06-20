# modelo/ingrediente.py

from datetime import date

class Ingrediente :

    def __init__ (self, nombre: str, cantidad: float, unidad: str, categoria: str, fecha_vencimiento: date, estado: str = "fresco") :
        
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad = unidad
        self.categoria = categoria
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado

    def esta_vencido(self) -> bool :

        return self.fecha_vencimiento < date.today()

    def __str__ (self) :
        
        return f"{self.nombre} ({self.cantidad} {self.unidad}) - Vence: {self.fecha_vencimiento}"
