#En este ejercicio practicarás las estructuras de control, para ello deberás crear:
#Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
#Pista: Los números inferiores a 0 son negativos y los superiores, positivos.

import logging
numero = input("Ingrese un número: ")
while True:
    if numero.isdigit() == True: #controlamos que sea números
        break
    else:
        logging.error("ERROR. Solo se aceptan números.")
        numero=input("Ingrese un número: ")         
numero = float(numero)
if numero == 0:
    print("El número es 0")
elif numero > 0:
    print("El número es mayor a 0")
else:
    print("El número es menor a 0")

#Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:
#Incrementar el valor de la variable en uno cada vez que se ejecute.
#Mostrarlo por pantalla cada vez que se ejecute.

#Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que la variable sea igual o menor que 3, se irá
#incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla.
#Por último, para el Switch, deberás crear la variable estación, y distintos case para las cuatro estaciones del año. Dependiendo del valor de la variable estación se deberá mandar 
#un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación.


numero_while = input("Ingrese un número: ")
while True:
    if numero_while.isdigit() == True: #controlamos que sea números
        break
    else:
        logging.error("ERROR. Solo se aceptan números.")
        numero=input("Ingrese un número: ") 
numero_while= float(numero_while)
while numero_while < 3:
    numero_while= numero_while + 1 
print(numero_while)






