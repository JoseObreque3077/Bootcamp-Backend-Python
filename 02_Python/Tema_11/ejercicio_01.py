import sqlite3

# Creación de conexión y cursor
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Creación de tabla
cursor.execute("CREATE TABLE Alumnos (id INT, Nombre TEXT, Apellido TEXT)")

# Datos de alumnos (8 alumnos)
nombres = ["Carlos",
           "Sergio",
           "Camila",
           "Sebastián",
           "José",
           "Romina",
           "Claudia",
           "Pedro"]
apellidos = ["Cifuentes",
             "Contreras",
             "Almonacid",
             "Toro",
             "Fuentes",
             "Figueroa",
             "Conserva",
             "Pérez"]

# Inserción de alumnos en la base de datos
id = 1
for nombre, apellido in zip(nombres, apellidos):
    query = f"INSERT INTO Alumnos (id, nombre, apellido) \
        VALUES ({id}, '{nombre}', '{apellido}')"
    cursor.execute(query)
    id += 1

# Guardado de cambios en la base de datos    
conn.commit()

# Búsqueda de un alumno por nombre
cursor.execute("SELECT * FROM Alumnos WHERE nombre='Sergio'")
alumnos_encontrados = cursor.fetchall()

for alumno in alumnos_encontrados:
    print(alumno)
    
# Cierre de cursor y base de datos
cursor.close()
conn.close()
