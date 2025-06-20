import customtkinter

def cambiar_color():
    """Cambia el color de fondo de la ventana."""
    nuevo_color = "red"  # Cambia a tu color deseado
    app.configure(fg_color=nuevo_color)

# Configuración de la ventana
app = customtkinter.CTk()
app.geometry("400x300")
app.title("Cambio de color con botón")

# Crear el botón
boton_cambiar_color = customtkinter.CTkButton(
    master=app,
    text="Cambiar color",
    command=cambiar_color
)
boton_cambiar_color.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()