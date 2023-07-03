#Dado un número entero positivo, escribir una función para determinar si es un número primo.
import math
import logging

def es_primo(numero):
    if numero < 2:
        return "No es número primo"
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return "No es número primo"
    return "Es número primo"


print("¡Bienvenido!")
num = input("Ingrese un número para verificar si es primo o no: ")
while True:
    if num.isdigit() == True:
        break
    else:
        logging.error ("ERROR. Solo se aceptan números que sean enteros.")
        num = input("Ingrese un número para verificar si es primo o no: ")
resultado = es_primo(int(num))
print(resultado)
