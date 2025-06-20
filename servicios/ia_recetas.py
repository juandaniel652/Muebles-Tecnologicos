# Lógica para generar recetas con IA
# servicios/ia_recetas.py

from modelo.receta import Receta
from modelo.ingrediente_receta import IngredienteReceta
import random

def generar_receta_con_ia(ingredientes: list[str]) -> Receta:
    nombre = f"Receta Creativa con {' y '.join(ingredientes[:2])}"
    tiempo = random.randint(15, 45)
    dificultad = random.choice(["Fácil", "Media", "Difícil"])
    etiquetas = ["generado", "creativo"]
    pasos = [
        "Paso 1: Preparar los ingredientes.",
        "Paso 2: Mezclar todo con amor.",
        "Paso 3: Cocinar a gusto.",
        "Paso 4: Servir y disfrutar."
    ]

    receta = Receta(nombre, tiempo, dificultad, etiquetas, pasos)

    for ing in ingredientes:
        receta.agregar_ingrediente(IngredienteReceta(ing, cantidad=1.0, unidad="unidad"))

    return receta
