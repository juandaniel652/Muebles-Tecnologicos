# Lógica para conectarse a APIs externas
# servicios/api_recetas.py

import requests
from modelo.receta import Receta
from modelo.ingrediente_receta import IngredienteReceta

API_KEY = "d0c834d07a724058bfffab484c79bc92"  # <-- Reemplaza con tu clave real

def obtener_recetas_desde_api(ingredientes: list[str], numero: int = 5) -> list[Receta]:
    recetas = []
    url = "https://api.spoonacular.com/recipes/findByIngredients"

    params = {
        "ingredients": ",".join(ingredientes),
        "number": numero,
        "ranking": 1,
        "ignorePantry": True,
        "apiKey": API_KEY
    }

    respuesta = requests.get(url, params=params)

    if respuesta.status_code != 200:
        print(f"Error al consultar la API: {respuesta.status_code}")
        return []

    datos = respuesta.json()

    for item in datos:
        receta_id = item["id"]
        titulo = item["title"]
        ingredientes_receta = []

        for ing in item["usedIngredients"] + item["missedIngredients"]:
            nombre = ing["name"]
            cantidad = ing.get("amount", 1.0)
            unidad = ing.get("unit", "")
            ingredientes_receta.append(IngredienteReceta(nombre, cantidad, unidad))

        pasos, tiempo = obtener_pasos_y_tiempo(receta_id)

        receta = Receta(
            nombre=titulo,
            tiempo=tiempo,
            dificultad="Media",
            etiquetas=[],
            pasos=pasos
        )
        for ingr in ingredientes_receta:
            receta.agregar_ingrediente(ingr)

        recetas.append(receta)

    return recetas

def obtener_pasos_y_tiempo(receta_id: int):
    url = f"https://api.spoonacular.com/recipes/{receta_id}/information"
    params = {"apiKey": API_KEY}
    respuesta = requests.get(url, params=params)

    if respuesta.status_code != 200:
        return [], 0

    data = respuesta.json()
    pasos = [s["step"] for s in data.get("analyzedInstructions", [{}])[0].get("steps", [])]
    tiempo = data.get("readyInMinutes", 0)
    return pasos, tiempo