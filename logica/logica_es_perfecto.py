#Dado un número entero positivo, escribir una función para determinar si es un número perfecto. Un número perfecto es aquel cuya 
#suma de sus divisores, exceptuando él mismo, es igual al número.

def es_perfecto(numero):
    cuenta=1
    resultado=0
    while numero >cuenta:
        if numero % cuenta == 0:
            resultado= resultado + cuenta
        cuenta= cuenta +1
    if resultado == numero:
        return "Es un número perfecto"
    else:
        return "No es un número perfecto"
    
num= input("Ingresa un número para verificar si es un número perfecto o no: ")
while True:
    if num.isdigit() == True:
        break
    else:
        print("ERROR. Solo se aceptan números enteros.")
        num= input("Ingresa un número para verificar si es un número perfecto o no: ")
resultado= es_perfecto(int(num))
print(resultado)  