#Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
#Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
import logging #importamos logging para error
logging.basicConfig(level=logging.INFO)
país= input("Ingrese un país para ingresarlo en la lista o 'fin' para terminar de ingresar países: ")
país=país.title() #lo ponemos en mayúscula
lista=[]

while país.lower() != "fin":
    
    if país.replace(" ", "").isalpha() == False : #mientras país sea diferente a letras, sacando los espacios
        logging.error("Error, los países solo pueden contener caracteres.")
        país= input("Ingrese un país para ingresarlo en la lista o 'fin' para terminar de ingresar países: ")
        país=país.title()
    
    else:
        lista.append(país) #si son letras, agregamos a la lista
        país= input("Ingrese un país para ingresarlo en la lista o 'fin' para terminar de ingresar países: ")
        país=país.title()

lista = set(lista) #borramos repetidos
lista= list(lista)
lista= sorted(lista) #ordenamos alfabéticamente

if len(lista) == 0: #si esta vacía la lista ocurre
    print ("No agrego nada a la lista.")
else:
    print("La lista de países es la siguiente: "+",".join(lista)+".")


