# interfaz/pestaña_ingredientes.py

import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from modelo.ingrediente import Ingrediente

class PestañaIngredientes (ctk.CTkFrame) :

    def __init__ (self, master, heladera) :

        super().__init__(master)
        self.heladera = heladera

        self.grid_columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(self, text="Agregar Ingrediente", font=ctk.CTkFont(size=16, weight="bold")).grid(row=0, column=0, columnspan=2, pady=10)

        self.entry_nombre = ctk.CTkEntry(self, placeholder_text="Nombre")
        self.entry_nombre.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.entry_cantidad = ctk.CTkEntry(self, placeholder_text="Cantidad (número)")
        self.entry_cantidad.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.entry_unidad = ctk.CTkEntry(self, placeholder_text="Unidad (g, ml, u, etc)")
        self.entry_unidad.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.entry_categoria = ctk.CTkEntry(self, placeholder_text="Categoría")
        self.entry_categoria.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        self.entry_fecha = ctk.CTkEntry(self, placeholder_text="Fecha venc. (AAAA-MM-DD)")
        self.entry_fecha.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        self.estado_opcion = ctk.CTkOptionMenu(self, values=["fresco", "cocido", "congelado"])
        self.estado_opcion.set("fresco")
        self.estado_opcion.grid(row=3, column=1, padx=10, pady=5)

        self.boton_agregar = ctk.CTkButton(self, text="Agregar", command=self.agregar_ingrediente)
        self.boton_agregar.grid(row=4, column=0, columnspan=2, pady=10)

        ctk.CTkLabel(self, text="Lista de Ingredientes", font=ctk.CTkFont(size=14, weight="bold")).grid(row=5, column=0, columnspan=2, pady=(20, 5))

        self.lista_ingredientes = ctk.CTkTextbox(self, height=200)
        self.lista_ingredientes.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        self.actualizar_lista()
 

    def agregar_ingrediente (self) :

        try :

            nombre = self.entry_nombre.get().strip()
            cantidad = float(self.entry_cantidad.get())
            unidad = self.entry_unidad.get().strip()
            categoria = self.entry_categoria.get().strip()
            fecha_str = self.entry_fecha.get().strip()
            fecha_venc = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            estado = self.estado_opcion.get()

            if not nombre :

                raise ValueError("Falta el nombre del ingrediente")

            nuevo = Ingrediente(nombre, cantidad, unidad, categoria, fecha_venc, estado)
            self.heladera.agregar_ingrediente(nuevo)
            self.actualizar_lista()
            self.limpiar_campos()

        except Exception as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")


    def limpiar_campos(self):
        self.entry_nombre.delete(0, 'end')
        self.entry_cantidad.delete(0, 'end')
        self.entry_unidad.delete(0, 'end')
        self.entry_categoria.delete(0, 'end')
        self.entry_fecha.delete(0, 'end')
        self.estado_opcion.set("fresco")


    def actualizar_lista(self):
        self.lista_ingredientes.delete("1.0", "end")
        for ing in self.heladera.ingredientes:
            estado = "⚠️ Vence pronto" if ing.esta_vencido() else ""
            self.lista_ingredientes.insert("end", f"{str(ing)} {estado}\n")