import time

# Hora actual extraida del sistema
hora_actual = int(time.strftime("%H"))
minuto_actual = int(time.strftime("%M"))

if (hora_actual >= 19):
    # Si son mas de las 19:00 no es horario laboral
    print("Ya no es horario laboral!")
else:
    # Si aún no son las 19:00 se muestra el tiempo laboral restante
    print(f"Tiempo laboral restante: {18-hora_actual} hrs {60-minuto_actual} min")
