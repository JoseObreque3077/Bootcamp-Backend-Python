# Clase padre
class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
# Clase hija
class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

# Instancia de clase Coche
coche = Coche("azul", 4, 4, 120, 1500)

# Atributos por consola
print(f"Color: {coche.color}")
print(f"Num. Ruedas: {coche.ruedas}")
print(f"Num. Puertas: {coche.puertas}")
print(f"Velocidad: {coche.velocidad}")
print(f"Cilindrada: {coche.cilindrada}")
