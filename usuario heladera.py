import tkinter as tk
from tkinter import ttk, END
import sqlite3
from tkinter import messagebox as mb
from tkinter import Text

class Aplicacion():
    
    
    def __init__(self):
        self.conexion = sqlite3.connect("bd3.db")
        self.ventana = tk.Tk()
        self.ventana.title("Heladera inteligente")
        self.ventana.geometry("500x400") 

        self.cuaderno = ttk.Notebook(self.ventana)
        self.cuaderno.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")

        self.ventana.columnconfigure(0, weight=1)
        self.ventana.rowconfigure(0, weight=1)

        self.agregar_usuario()
        self.consulta_por_codigo()
        self.listado_usuario()

        self.ventana.mainloop()

    def agregar(self):
        pass
    def agregar_usuario(self):
        self.conexion = sqlite3.connect("bd3.db")
        self.pagina1 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina1, text="Carga Usuario")
        
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Usuario")
        self.labelframe1.grid(column=0, row=0, padx=20, pady=20, sticky="nsew")

        self.pagina1.columnconfigure(0, weight=1)
        self.labelframe1.columnconfigure(1, weight=1)

        # Nombre
        ttk.Label(self.labelframe1, text="Nombre:").grid(column=0, row=0, padx=4, pady=4, sticky="e")
        self.dato1 = tk.StringVar()
        ttk.Entry(self.labelframe1, width=30, textvariable=self.dato1).grid(column=1, row=0, padx=4, pady=4, sticky="ew")

        # Edad
        ttk.Label(self.labelframe1, text="Edad:").grid(column=0, row=1, padx=4, pady=4, sticky="e")
        self.dato2 = tk.IntVar()
        ttk.Entry(self.labelframe1, width=30, textvariable=self.dato2).grid(column=1, row=1, padx=4, pady=4, sticky="ew")

        # Vegetariano
        self.es_vegetariano = tk.BooleanVar()
        ttk.Checkbutton(self.labelframe1, text="¿Es vegetariano?", variable=self.es_vegetariano)\
            .grid(column=0, row=2, columnspan=2, padx=4, pady=4, sticky="w")

        # Gustos personales
        ttk.Label(self.labelframe1, text="Gustos personales:").grid(column=0, row=3, padx=4, pady=4, sticky="e")
        self.gustos = tk.StringVar()
        ttk.Entry(self.labelframe1, width=30, textvariable=self.gustos).grid(column=1, row=3, padx=4, pady=4, sticky="ew")

        # Alergias alimenticias
        ttk.Label(self.labelframe1, text="Alergias alimenticias:").grid(column=0, row=4, padx=4, pady=4, sticky="e")
        self.alergias = tk.StringVar()
        ttk.Entry(self.labelframe1, width=30, textvariable=self.alergias).grid(column=1, row=4, padx=4, pady=4, sticky="ew")

        # Confirmar
        ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)\
            .grid(column=0, row=5, columnspan=2, pady=10)


    def consulta_por_codigo(self):
        self.conexion = sqlite3.connect("bd3.db")
        self.pagina2 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina2, text="Consulta por Usuario")
        self.labelframe2 = ttk.LabelFrame(self.pagina2, text="Usuario")
        self.labelframe2.grid(column=0, row=0, padx=10, pady=5)
        self.label2=ttk.Label(self.labelframe2, text="Código: ")
        self.label2.grid(column=0, row=0, padx=4, pady=4)
        self.dato_cod = tk.StringVar()
        self.entry_codigo=ttk.Entry(self.labelframe2, width=15, textvariable=self.dato_cod)
        self.entry_codigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe2, text="Descripción: ")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.entry_desc=ttk.Entry(self.labelframe2)
        self.entry_desc.grid(column=1, row=1, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe2, text="nombre: ")
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.entry_precio=ttk.Entry(self.labelframe2)
        self.entry_precio.grid(column=1, row=2, padx=4, pady=4)
        self.boton2=ttk.Button(self.labelframe2, text="Confirmar", command=self.consultar)
        self.boton2.grid(column=1, row=3, padx=4, pady=4)
        
    def consultar(self):
        self.conexion = sqlite3.connect("bd3.db")
        cursor = self.conexion.execute("select descripcion, usuario from usuarios where codigo=?", (int(self.dato_cod.get()),))
        fila = cursor.fetchone()
        
        if fila:
            self.entry_desc.configure(state="normal")
            self.entry_desc.delete(0, END)
            self.entry_desc.insert(END, fila[0])
            self.entry_desc.configure(state="disabled")
            
            self.entry_precio.configure(state="normal")
            self.entry_precio.delete(0, END)
            self.entry_precio.insert(END, fila[1])
            self.entry_precio.configure(state="disabled")
        else:
            mb.showinfo("Información", "No se encontró el usuario.")
        
        self.conexion.close()
    
    def listado_usuario(self):
        self.conexion = sqlite3.connect("bd3.db")
        self.pagina3 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina3, text="Listado de Usuario")
        self.labelframe3 = ttk.LabelFrame(self.pagina3, text="Usuarios")
        self.labelframe3.grid(column=0, row=0, padx=10, pady=5)
        self.scroll1 = ttk.Scrollbar(self.labelframe3, orient=tk.VERTICAL)
        self.listbox1 = tk.Listbox(self.labelframe3, selectmode=tk.MULTIPLE, yscrollcommand=self.scroll1.set)
        self.listbox1.grid(column=0, row=1)
        self.scroll1.configure(command=self.listbox1.yview)
        self.scroll1.grid(column=1, row=1, sticky='NS')

        self.boton4 = ttk.Button(self.pagina3, text="Listado de Usuario", command=self.Listado_completo)
        self.boton4.grid(column=0, row=1)
        self.label4 = ttk.Label(self.pagina3, text="Seleccionado:")
        self.label4.grid(column=0, row=2)
        
    def Listado_completo(self):
        self.conexion = sqlite3.connect("bd3.db")
        self.listbox1.delete(0, END)  
        cursor = self.conexion.execute("SELECT codigo")
        
        for fila in cursor:
            
            self.listbox1.insert(END, f"Código: {fila[0]}, Descripción: {fila[1]}, Precio: {fila[2]}")
        
        self.conexion.close()

app = Aplicacion()
