class Alumno:
    # Constructor (método inicializador)
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    # Método para mostrar info por consola
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
    
    # Método que muestra la nota e indica si aprueba o no
    def verificar_aprobacion(self):
        print(f"Nota: {self.nota}")
        if self.nota < 4:
            print("Estado: Reprobado")
        else:
            print("Estado: Aprobado")


# Instancias de clase
alumno1 = Alumno("Carlos", 6.5)
alumno2 = Alumno("Carolina", 3.8)

# Datos de cada alumno por consola
alumno1.mostrar_info()
alumno2.mostrar_info()

# Estado de aprobación de cada alumno
alumno1.verificar_aprobacion()
alumno2.verificar_aprobacion()
