
#Ejemplo de uso de las tres funciones en conjunto:
#Escribe un programa que lea una lista de números, filtre los números que son divisibles por 3 utilizando la función filter(), eleve al cubo los números resultantes u
#utilizando la función map(), y finalmente sume los números elevados al cubo utilizando la función reduce(). Muestra el resultado final de la suma.
from functools import reduce 

números=input("Ingrese números a la lista. En caso de de ingresar otra cosa que no sean números, se borrara de la lista. Ingrese 'fin' para terminar: ")
lista = []
#creamos lista con números y todo lo que agregue
while números.lower() != "fin":
    lista.append(números)
    números=input("Ingrese números a la lista. En caso de de ingresar otra cosa que no sean números, se borrara de la lista. Ingrese 'fin' para terminar: ")
#función que, mientras sea float devuelve true a menos que halla valueError que da false
def es_flotante(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
#función que borra todo lo que no sea números
def borrar_no_números(lista):
    lista_actualizada = []
    for elemento in lista:
        if isinstance(elemento, (int, float)): #isinstance agarra un elemento y permite que sea de dos tipos. En este caso, int y float
            lista_actualizada.append(elemento)
        elif isinstance(elemento, str) and elemento.isnumeric(): #si el elemento es str y ademas es dígito lo deja
            lista_actualizada.append(int(elemento))
        elif isinstance(elemento, str) and es_flotante(elemento): #si el elemento es str y es flotante (gracias a la otra función) lo deja
            lista_actualizada.append(float(elemento))
    return lista_actualizada

lista_actualizada= borrar_no_números(lista)
lista_actualizada= list(lista_actualizada)
def divisibles(x):
    if x %3 == 0:
        return True
    else:
        return False

lista_divisible= filter(divisibles,lista_actualizada)
lista_divisible = list(lista_divisible)
def al_cubo(x):
    return x**3

lista_al_cubo = map(al_cubo,lista_divisible)
lista_al_cubo = list(lista_al_cubo)
def suma(a,b):
    return a+b

número_final = reduce(suma,lista_al_cubo)

print("Lista con todos lo agregado:")
print(lista)
print("Lista con solo números: ")
print(lista_actualizada)
print("Lista de números divisibles por 3: ")
print(lista_divisible)
print("Lista de números elevados al cubo: ")
print(lista_al_cubo)
print("Suma total: "+str(número_final))
