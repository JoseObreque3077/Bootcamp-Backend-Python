# Se crea el fichero, con una sola línea de texto (en modo solo escritura)
file = open("fichero_01.txt", "w")
file.write("He creado un archivo txt!\n")
file.close()

# Se abre el fichero, en modo lectura-append y se agrega una segunda línea
file = open("fichero_01.txt", "a+")
file.write("He agregado una segunda línea")

# Se inicia la lectura al inicio del fichero, para mostrar todo su contenido
file.seek(0)
print(file.read())
file.close()
