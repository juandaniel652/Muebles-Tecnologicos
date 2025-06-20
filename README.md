# 🧊 Heladera Inteligente

Una aplicación que transforma tu heladera en un asistente culinario inteligente. Sugiere recetas automáticamente en base a los **ingredientes disponibles**, tus **gustos personales**, **alergias** y **preferencias alimenticias**.

---

## 📌 Objetivo

Ayudar al usuario a optimizar sus alimentos disponibles y reducir desperdicios, recomendando recetas basadas en:

- Ingredientes en la heladera (con cantidad y vencimiento)
- Preferencias personales (vegetariano, sin gluten, etc.)
- Alergias o ingredientes excluidos
- Gustos (dulce, salado, picante, etc.)
- Tiempo de cocción disponible

---

## 🧱 Arquitectura y diseño

El proyecto está desarrollado en Python utilizando principios de Programación Orientada a Objetos (POO) y diseño limpio.  
El sistema se basa en las siguientes clases:

- `Ingrediente`: representa un ingrediente con su estado y vencimiento
- `IngredienteReceta`: cantidad necesaria de un ingrediente en una receta
- `Receta`: contiene los pasos y los ingredientes requeridos
- `Usuario`: guarda preferencias, alergias y gustos
- `HeladeraInteligente`: motor principal que relaciona ingredientes, recetas y usuario

Diagrama UML disponible en el repositorio.

---

## 🛠️ Tecnologías usadas

- Python 3.x
- Estructura modular basada en OOP
- (Opcional) Pandas / SQLite para persistencia de datos
- (Opcional) Tkinter / PyQt para interfaz gráfica

---

## 🚀 Funcionalidades clave

- ✅ Sugerencia de recetas con los ingredientes actuales
- ⚠️ Alertas de ingredientes por vencer
- 🛒 Sugerencias de compras mínimas para completar recetas
- 🔍 Filtro por preferencias y restricciones alimenticias
- 🕐 Filtro por tiempo de cocción
