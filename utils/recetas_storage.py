# utils/recetas_storage.py

import json
from modelo.receta import Receta
from modelo.ingrediente_receta import IngredienteReceta

ARCHIVO = "recetas_guardadas.json"

def guardar_recetas(recetas: list[Receta]):
    serializadas = []
    for r in recetas:
        serializadas.append({
            "nombre": r.nombre,
            "tiempo": r.tiempo,
            "dificultad": r.dificultad,
            "etiquetas": r.etiquetas,
            "pasos": r.pasos,
            "ingredientes": [
                {"nombre": i.nombre, "cantidad": i.cantidad, "unidad": i.unidad}
                for i in r.ingredientes
            ]
        })
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(serializadas, f, ensure_ascii=False, indent=4)

def cargar_recetas() -> list[Receta]:
    recetas = []
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            data = json.load(f)
            for r in data:
                receta = Receta(r["nombre"], r["tiempo"], r["dificultad"], r["etiquetas"], r["pasos"])
                for i in r["ingredientes"]:
                    receta.agregar_ingrediente(IngredienteReceta(i["nombre"], i["cantidad"], i["unidad"]))
                recetas.append(receta)
    except FileNotFoundError:
        pass
    return recetas
