from pickle import dump, load


class Vehiculo:
    def __init__(self, marca, num_puertas):
        self.marca = marca
        self.num_puertas = num_puertas

    def __str__(self):
        return f"Marca: {self.marca}\nPuertas: {self.num_puertas}"


# Instancia de la clase
vehiculo = Vehiculo("Kia", 2)
print(vehiculo)

# Se crea un fichero .bin para almacenar un objeto de tipo Vehiculo
file = open("fichero_02.bin", "wb+")
dump(vehiculo, file)

# Se crea un nuevo objeto de la clase Vehiculo a partir del objeto almacenado
file.seek(0) # Se inicia la lectura al inicio del fichero
nuevo_vehiculo = load(file)
print(nuevo_vehiculo)

file.close()
