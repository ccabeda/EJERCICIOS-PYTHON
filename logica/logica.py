#Crea una función que calcule los números primos entre 1 y N, siendo N el parámetro que recibe la función.
import math
def calculo(numero):
    lista=[]
    inicial=1
    números_primos=[]
    while numero >inicial:
        lista.append(numero)
        inicial=inicial+1
    for i in lista:
        for j in range(2, int(math.sqrt(numero)) + 1):
            if i % j == 0:
                break
        else:
            números_primos.append(i)
    
    return números_primos
        




