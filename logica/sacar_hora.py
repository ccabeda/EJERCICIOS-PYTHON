import time

hora_actual = time.localtime().tm_hour

if hora_actual >= 19:
    print("Es hora de ir a casa.")
else:
    tiempo_restante = (19 - hora_actual) * 60  # Calculamos el tiempo restante en minutos
    print(f"Aún quedan {tiempo_restante} minutos para ir a casa.")