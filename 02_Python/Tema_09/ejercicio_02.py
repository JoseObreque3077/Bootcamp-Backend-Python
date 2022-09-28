from functools import reduce


# Función que calcula la sumatoria de los valores impares de una lista de
# números enteros entregada como parámetro
def suma_impares(valores):
    impares = list(filter(lambda x: x % 2 != 0, valores))
    resultado = reduce(lambda x, y: x + y, impares)
    return resultado


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(suma_impares(numeros)) # 1+3+5+7+9=25
