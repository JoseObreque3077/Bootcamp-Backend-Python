import tkinter
from tkinter import END, ttk

window = tkinter.Tk()

# Etiqueta
label = ttk.Label(window, text="Lista de mascotas disponibles:")
label.pack()

# Lista
mascotas = ["perro", "gato", "canario",
            "conejo", "hamster", "serpiente", "loro"]
listado = tkinter.Listbox(window)

for mascota in mascotas:
    listado.insert(END, mascota)

listado.pack()

window.mainloop()
