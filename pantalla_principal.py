# interfaz/pantalla_principal.py

import customtkinter as ctk
from interfaz.pestana_ingredientes import PestañaIngredientes
from interfaz.pestana_recetas import PestañaRecetas
from interfaz.pestana_usuario import PestanaUsuario

class PantallaPrincipal (ctk.CTkFrame) :

    def __init__ (self, master, heladera) :

        super().__init__(master)
        self.heladera = heladera

        self.pestanas = ctk.CTkTabview(self)
        self.pestanas.pack(fill="both", expand=True, padx=20, pady=20)

        # Pestaña Usuario
        self.pestana_usuario = self.pestanas.add("Usuario")
        self.pestania_usuario = PestanaUsuario(self.pestana_usuario, self.heladera)
        self.pestania_usuario.pack(fill="both", expand=True)

        # Pestaña Ingredientes
        self.pestana_ingredientes = self.pestanas.add("Ingredientes")
        self.pestania_ingredientes = PestañaIngredientes(self.pestana_ingredientes, self.heladera)
        self.pestania_ingredientes.pack(fill="both", expand=True)

        # Pestaña Recetas
        self.pestana_recetas = self.pestanas.add("Recetas")
        self.pestania_recetas = PestañaRecetas(self.pestana_recetas, self.heladera)
        self.pestania_recetas.pack(fill="both", expand=True)