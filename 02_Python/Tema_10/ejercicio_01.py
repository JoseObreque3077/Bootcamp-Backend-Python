import tkinter
from tkinter import ttk


# Asignación de texto a etiqueta de respuesta
def mostrar_respuesta():
    label_respuesta.config(text=f"Tu respuesta es: {respuesta.get()}")


# Reinicio de radiobuttons y etiqueta de respuesta
def reiniciar():
    respuesta.set(None)
    label_respuesta.config(text="")


window = tkinter.Tk()

# Label de título
label_pregunta = ttk.Label(window, text="¿En que continente vives?")
label_pregunta.pack()

# Generación de radiobuttons
continentes = ["Asia", "América", "África", "Antártida", "Europa", "Oceanía"]
respuesta = tkinter.StringVar()

for continente in continentes:
    rb = ttk.Radiobutton(window,
                         text=continente,
                         value=continente,
                         variable=respuesta,
                         command=mostrar_respuesta)
    rb.pack()

# Etiqueta con opcion seleccionada
label_respuesta = ttk.Label(window)
label_respuesta.pack()

# Botón de reinicio
reset = ttk.Button(text="Reset", command=reiniciar)
reset.pack()

window.mainloop()
