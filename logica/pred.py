#Escribe un programa que lea una lista de números, filtre los números pares utilizando la función filter(), eleve al cuadrado los números resultantes utilizando la 
# función map(), y finalmente sume los números elevados al cuadrado utilizando la función reduce(). Muestra el resultado final de la suma.

from functools import reduce
import logging
logging.basicConfig(level=logging.INFO)

números=input("Ingrese números a una lista y cualquier letra para terminar de hacerlo: ")
lista=[]
#mientras no sea una letra que entre
while números.isalpha() == False :
    if números.isdigit() == True: #si es un número que lo agregue y siga
        lista.append(int(números))
        números=input("Ingrese números a una lista y cualquier letra para terminar de hacerlo: ")
    else: #si es otro carácter que salte error y siga
        logging.error(" ERROR. Usted ingreso un carácter invalido, solo se permiten letras y números")
        números=input("Ingrese números a una lista y cualquier letra para terminar de hacerlo: ")

def pares(x):
    if x %2 ==0:
        return True
    else:
        return False

num_pares = filter(pares,lista)
num_pares= list(num_pares)

def al_cuadrado(x):
    return x**2

elevadas=map(al_cuadrado,num_pares)
elevadas=list(elevadas)

def suma(a,b):
    return a+b

final= reduce(suma,elevadas)

print(lista)
print(num_pares)
print(elevadas)
print(final)
