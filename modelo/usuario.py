# modelo/usuario.py

from modelo.receta import Receta

class Usuario :

    def __init__ (self, nombre: str, preferencias: list[str] = None, alergias: list[str] = None, gustos: list[str] = None, excluidos: list[str] = None) :
        
        self.nombre = nombre
        self.preferencias = preferencias or []
        self.alergias = alergias or []
        self.gustos = gustos or []
        self.excluidos = excluidos or []


    def puede_comer (self, receta: Receta) -> bool :

        for ingrediente in receta.ingredientes :

            nombre_ingrediente = ingrediente.nombre.lower()

            if nombre_ingrediente in [alergia.lower() for alergia in self.alergias] :

                return False
            
            if nombre_ingrediente in [excluido.lower() for excluido in self.excluidos] :

                return False
            
        return True


    def __str__ (self) :
        
        return f"{self.nombre} (Preferencias: {', '.join(self.preferencias)})"
