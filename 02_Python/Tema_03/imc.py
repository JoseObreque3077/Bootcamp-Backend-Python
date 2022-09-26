peso = float(input("Ingrese su peso en Kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

imc = peso / (estatura ** 2)

print(f"Tu IMC es: {round(imc, 2)}")
