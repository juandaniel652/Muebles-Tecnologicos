import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from modelo.usuario import Usuario

class PestanaUsuario (ctk.CTkFrame) :

    def __init__ (self, master, heladera) :
        
        super().__init__(master)
        self.heladera = heladera

        # Crear widgets con placeholder

        self.label_nombre = ctk.CTkLabel(self, text="Nombre:")
        self.entry_nombre = ctk.CTkEntry(self, placeholder_text="Ingrese el nombre")
        self.label_preferencias = ctk.CTkLabel(self, text="Preferencias:")
        self.entry_preferencias = ctk.CTkEntry(self, placeholder_text="Ej: vegetariano, sin azúcar")
        self.label_alergias = ctk.CTkLabel(self, text="Alergias:")
        self.entry_alergias = ctk.CTkEntry(self, placeholder_text="Ej: maní, gluten")
        self.label_gustos = ctk.CTkLabel(self, text="Gustos:")
        self.entry_gustos = ctk.CTkEntry(self, placeholder_text="Ej: chocolate, queso")
        self.label_excluidos = ctk.CTkLabel(self, text="Excluidos:")
        self.entry_excluidos = ctk.CTkEntry(self, placeholder_text="Ej: pescado, huevo")

        self.boton_guardar = ctk.CTkButton(self, text="Guardar Usuario", command=self.guardar_usuario)
        self.boton_cambiar_fondo = ctk.CTkButton(self, text = "Cambiar Fondo", command= self.cambiar_fondo)
        self.boton_reestablecer_fondo = ctk.CTkButton(self, text = "Reestablecer Fondo", command= self.reestablecer_fondo)


        # Ubicar widgets
        lista_widgets = [self.label_nombre, self.entry_nombre, self.label_preferencias,
                        self.entry_preferencias, self.label_alergias, self.entry_alergias,
                        self.label_gustos, self.entry_gustos, self.label_excluidos, 
                        self.entry_excluidos]
        
        lista_sticky = ["w", "ew", "w", "ew", "w", "ew", "w", "ew", "w", "ew"]
        lista_fila = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
        lista_columna = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
        
        for indice, widget in enumerate (lista_widgets) : 

            fila = lista_fila[indice]
            columna = lista_columna[indice]
            lugar_cuadricula = lista_sticky[indice]
            
            widget.grid(row = fila, column = columna, padx = 10, pady = 5, sticky = lugar_cuadricula)

        self.boton_guardar.grid(row = 5, column = 0, columnspan = 2, pady = 15)
        self.boton_cambiar_fondo.grid(row = 6, column = 0, columnspan = 2, pady = 15)
        self.boton_reestablecer_fondo.grid(row = 7, column = 0, columnspan = 2, pady = 15)
        self.grid_columnconfigure(1, weight=1)


    def guardar_usuario (self) :

        nombre = self.entry_nombre.get()
        preferencias = [preferencia.strip() for preferencia in self.entry_preferencias.get().split(",") if preferencia.strip()]
        alergias = [alergia.strip() for alergia in self.entry_alergias.get().split(",") if alergia.strip()]
        gustos = [gusto.strip() for gusto in self.entry_gustos.get().split(",") if gusto.strip()]
        excluidos = [excluido.strip() for excluido in self.entry_excluidos.get().split(",") if excluido.strip()]

        if not nombre :

            messagebox.showerror("Error", "El nombre no puede estar vacío.")
            return

        usuario = Usuario(nombre, preferencias, alergias, gustos, excluidos)

        # Aquí puedes agregar el usuario a la heladera o hacer lo que necesites
        messagebox.showinfo("Éxito", f"Bienvenido '{nombre}'! Tus datos se han guardado correctamente.")


    def cambiar_fondo (self) : 

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")


    def reestablecer_fondo (self) : 

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")