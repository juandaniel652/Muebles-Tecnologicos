# main.py

import customtkinter as ctk
from pantalla_principal import PantallaPrincipal
from sistema.heladera import HeladeraInteligente
from modelo.usuario import Usuario
from utils.recetas_storage import cargar_recetas

def main() :
     
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")  # o "dark-blue", "green", etc.

    app = ctk.CTk()
    app.title("Heladera Inteligente")
    app.geometry("900x600")
    app.resizable(False, False)

    usuario = Usuario(nombre="Invitado")
    heladera = HeladeraInteligente(usuario)
    heladera.recetas = cargar_recetas()

    pantalla = PantallaPrincipal(app, heladera)
    pantalla.pack(fill="both", expand=True)

    app.mainloop()

if __name__ == "__main__":
    main()