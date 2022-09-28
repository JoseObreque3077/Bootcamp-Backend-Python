entrada_usuario = input("Ingrese una lista de países, separados por comas: ")

paises = set([pais.strip().title() for pais in entrada_usuario.split(",")])

print(f"Países ingresados: {', '.join(sorted(list(paises)))}")