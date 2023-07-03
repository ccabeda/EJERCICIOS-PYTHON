#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con 
#filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
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
#borramos repetidos
lista= set(lista)
lista= list(lista)
#función que da impares
def números_impares(x):
    if x % 2 != 0:
        return True
    else:
        return False
#borramos los números pares con filter (solo acepta funciones que devuelvan true o false)
impares= filter(números_impares,lista)
impares = list(impares)
#función sumar
def sumar(a,b):
    return a+b
#los sumamos con reduce ya importada
elementos= reduce(sumar,impares)
print(lista)
print(impares)
print(elementos)
