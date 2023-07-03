#En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.
#Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.
#importamos del modulo operaciones las funciones que queremos usar
from operaciones import suma,resta,div,multi

#MENÚ DEFAULT DE OPCIONES 
while True:
    print("Ingrese el número correspondiente a la operación que desea realizar:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")
    print("5. Salir")
    # Pedimos la operación al usuario
    operación = input("Operación que desea realizar: ")
    if operación == "1":
        # Acciones correspondientes a la opción 1
        print("Ha seleccionado la opción 1.")
        numero_uno=float(input("Ingrese el primer número que quiere sumar: "))
        numero_dos=float(input("Ingrese el segundo número que quiere sumar: "))
        print("El resultado de la suma es :"+str(suma(numero_uno,numero_dos)))
    elif operación == "2":
        # Acciones correspondientes a la opción 2
        print("Ha seleccionado la opción 2.")
        numero_uno=float(input("Ingrese el primer número que quiere restar: "))
        numero_dos=float(input("Ingrese el segundo número que quiere restar: "))
        print("El resultado de la resta es :"+str(resta(numero_uno,numero_dos)))
    elif operación == "3":
        # Acciones correspondientes a la opción 3
        print("Ha seleccionado la opción 3.")
        numero_uno=float(input("Ingrese el primer número que quiere dividir: "))
        numero_dos=float(input("Ingrese el segundo número que quiere dividir: "))
        print("El resultado de la división es :"+str(div(numero_uno,numero_dos)))
    elif operación == "4":
        # Acciones correspondientes a la opción 4
        print("Ha seleccionado la opción 4.")
        numero_uno=float(input("Ingrese el primer número que quiere multiplicar: "))
        numero_dos=float(input("Ingrese el segundo número que quiere multiplicar: "))
        print("El resultado de la multiplicación es :"+str(multi(numero_uno,numero_dos)))
    elif operación == "5":
        # Acciones correspondientes a la opción 5
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")


"""
#MENÚ 2 
#pedimos los datos
número_uno= float(input("Ingrese el primero número: "))
número_dos=float(input("Ingrese el segundo número: "))
#pedimos la operaciones
operación=input("Ingrese 1 para sumar, 2 para restar, 3 para dividir y 4 para multiplicar: ")

while True:
    if operación == "1":
        break
    elif operación == "2":
        break
    elif operación == "3":
        break
    elif operación == "4":
        break
    else:
        print("Error, debe ingresar un número del 1 al 4.")
        operación=input("Ingrese 1 para sumar, 2 para restar, 3 para dividir y 4 para multiplicar: ")

match operación:
    case "1":
        print(suma(número_uno,número_dos))
    case "2":
        print(resta(número_uno,número_dos))
    case "3":
        print(div(número_uno,número_dos))
    case "4":
        print(multi(número_uno,número_dos))"""

