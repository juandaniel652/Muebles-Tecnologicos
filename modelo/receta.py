# modelo/receta.py

from modelo.ingrediente_receta import IngredienteReceta

class Receta :

    def __init__ (self, nombre: str, tiempo: int, dificultad: str, etiquetas: list[str], pasos: list[str]) :

        self.nombre = nombre
        self.tiempo = tiempo  # en minutos
        self.dificultad = dificultad  # Fácil, Media, Difícil
        self.etiquetas = etiquetas  # ["vegano", "sin gluten", etc.]
        self.pasos = pasos
        self.ingredientes: list[IngredienteReceta] = []


    def agregar_ingrediente (self, ingrediente: IngredienteReceta) :

        self.ingredientes.append(ingrediente)


    def verificar_disponibilidad (self, ingredientes_disponibles: list) -> bool :

        disponibles = {ing.nombre.lower(): ing for ing in ingredientes_disponibles}

        for ing_receta in self.ingredientes :

            nombre = ing_receta.nombre.lower()

            if nombre not in disponibles or disponibles[nombre].cantidad < ing_receta.cantidad:
                
                return False
            
        return True


    def ingredientes_faltantes (self, ingredientes_disponibles: list) -> list :

        faltantes = []
        disponibles = {ing.nombre.lower(): ing for ing in ingredientes_disponibles}
        
        for ing_receta in self.ingredientes :

            nombre = ing_receta.nombre.lower()
            
            if nombre not in disponibles or disponibles[nombre].cantidad < ing_receta.cantidad:
            
                faltantes.append(ing_receta.nombre)
        
        return faltantes


    def __str__ (self) :

        return f"{self.nombre} ({self.dificultad}) - {self.tiempo} min"