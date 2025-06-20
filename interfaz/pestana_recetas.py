# interfaz/pestaña_recetas.py

import customtkinter as ctk
from servicios.api_recetas import obtener_recetas_desde_api
from servicios.ia_recetas import generar_receta_con_ia
from utils.recetas_storage import guardar_recetas
from tkinter import messagebox

class PestañaRecetas(ctk.CTkFrame):
    def __init__(self, master, heladera):
        super().__init__(master)
        self.heladera = heladera

        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self, text="Recetas Disponibles", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

        self.texto_recetas = ctk.CTkTextbox(self, height=300)
        self.texto_recetas.pack(fill="both", expand=True, padx=10, pady=10)
        self.texto_recetas.bind("<Double-Button-1>", self.mostrar_detalles_receta)

        self.boton_local = ctk.CTkButton(self, text="Buscar Recetas (Locales)", command=self.mostrar_recetas)
        self.boton_local.pack(pady=5)

        self.boton_faltantes = ctk.CTkButton(self, text="Sugerencias con pocos faltantes", command=self.mostrar_faltantes)
        self.boton_faltantes.pack(pady=5)

        self.boton_api = ctk.CTkButton(self, text="🔍 Buscar recetas desde API", command=self.buscar_desde_api)
        self.boton_api.pack(pady=10)

        self.recetas_mostradas = []

    def mostrar_recetas(self):
        self.texto_recetas.delete("1.0", "end")
        self.recetas_mostradas.clear()
        recetas = self.heladera.buscar_recetas_disponibles()
        if not recetas:
            self.texto_recetas.insert("end", "No hay recetas posibles con los ingredientes actuales.\n")
            return

        for idx, receta in enumerate(recetas):
            self.texto_recetas.insert("end", f"[{idx+1}] ✅ {receta.nombre} - {receta.tiempo} min - {receta.dificultad}\n")
            self.recetas_mostradas.append(receta)

    def mostrar_faltantes(self):
        self.texto_recetas.delete("1.0", "end")
        sugerencias = self.heladera.recetas_con_faltantes()
        self.recetas_mostradas.clear()
        if not sugerencias:
            self.texto_recetas.insert("end", "No hay recetas con solo 1 o 2 ingredientes faltantes.\n")
            return

        for idx, (receta, faltantes) in enumerate(sugerencias):
            faltantes_str = ", ".join(faltantes)
            self.texto_recetas.insert("end", f"[{idx+1}] 🔸 {receta.nombre} (Faltan: {faltantes_str})\n")
            self.recetas_mostradas.append(receta)

    def mostrar_detalles_receta(self, event):
        try:
            index = self._extraer_indice_desde_texto()
            if index is None or index >= len(self.recetas_mostradas):
                return
            receta = self.recetas_mostradas[index]

            ventana = ctk.CTkToplevel(self)
            ventana.title(receta.nombre)
            ventana.geometry("500x450")

            texto = f"Tiempo: {receta.tiempo} min\nDificultad: {receta.dificultad}\n\nIngredientes:\n"
            for i in receta.ingredientes:
                texto += f"• {i}\n"
            texto += "\nPasos:\n" + "\n".join([f"{i+1}. {p}" for i, p in enumerate(receta.pasos)])

            cuadro = ctk.CTkTextbox(ventana)
            cuadro.insert("1.0", texto)
            cuadro.configure(state="disabled")
            cuadro.pack(fill="both", expand=True, padx=10, pady=10)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo mostrar la receta: {e}")

    def _extraer_indice_desde_texto(self):
        try:
            linea = self.texto_recetas.get("insert linestart", "insert lineend")
            if linea.startswith("[") and "]" in linea:
                index_str = linea[1:linea.index("]")]
                return int(index_str) - 1
        except:
            pass
        return None

    def buscar_desde_api(self):
        self.texto_recetas.delete("1.0", "end")
        ingredientes_disponibles = [i.nombre for i in self.heladera.ingredientes]

        if not ingredientes_disponibles:
            self.texto_recetas.insert("end", "No hay ingredientes cargados.\n")
            return

        self.texto_recetas.insert("end", "Buscando recetas en la API...\n")
        self.recetas_mostradas.clear()

        try:
            nuevas_recetas = obtener_recetas_desde_api(ingredientes_disponibles)
            if not nuevas_recetas:
                raise Exception("Sin resultados")
            self.texto_recetas.insert("end", f"{len(nuevas_recetas)} receta(s) agregadas desde API:\n")
        except Exception as e:
            self.texto_recetas.insert("end", f"⚠️ Falló la API ({e}). Generando receta con IA...\n")
            receta = generar_receta_con_ia(ingredientes_disponibles)
            nuevas_recetas = [receta]

        self.heladera.recetas.extend(nuevas_recetas)
        guardar_recetas(self.heladera.recetas)

        for idx, r in enumerate(nuevas_recetas):
            self.texto_recetas.insert("end", f"[{idx+1}] 🧠 {r.nombre} - {r.tiempo} min - {r.dificultad}\n")
            self.recetas_mostradas.extend(nuevas_recetas)
