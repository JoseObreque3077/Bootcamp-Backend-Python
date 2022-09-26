# Función que muestra por consola si un año es bisiesto o no
def es_bisiesto(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")


es_bisiesto(1992) # Bisiesto
es_bisiesto(2000) # Bisiesto
es_bisiesto(1900) # No bisiesto
