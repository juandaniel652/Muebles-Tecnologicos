# sistema/heladera.py

from modelo.ingrediente import Ingrediente
from modelo.receta import Receta
from modelo.usuario import Usuario
from datetime import date

class HeladeraInteligente :

    def __init__ (self, usuario: Usuario) :

        self.usuario = usuario
        self.ingredientes: list[Ingrediente] = []
        self.recetas: list[Receta] = []


    def agregar_ingrediente (self, ingrediente: Ingrediente) :

        self.ingredientes.append(ingrediente)


    def agregar_receta (self, receta: Receta) :

        self.recetas.append(receta)


    def buscar_recetas_disponibles (self) -> list[Receta] :

        disponibles = []

        for receta in self.recetas :

            if self.usuario.puede_comer(receta) and receta.verificar_disponibilidad(self.ingredientes):
                
                disponibles.append(receta)

        return disponibles


    def recetas_con_faltantes(self) -> list[tuple[Receta, list[str]]] :

        sugerencias = []

        for receta in self.recetas :

            if self.usuario.puede_comer(receta) :

                faltan = receta.ingredientes_faltantes(self.ingredientes)

                if faltan and len(faltan) <= 2:  # tolera sugerencias con 1 o 2 faltantes
                    
                    sugerencias.append((receta, faltan))

        return sugerencias
    

    def ingredientes_por_vencer (self) -> list[Ingrediente] :

        proximos = []

        for ingrediente in self.ingredientes :

            if 0 <= (ingrediente.fecha_vencimiento - date.today()).days <= 3 :

                proximos.append(ingrediente)

        return proximos
