#Ejercicio 2
#Enunciado: Crea una agenda de teléfonos que se gestione por consola, que te permita:
#Añadir a cualquier persona, indicando nombre y después teléfono
#Buscar el teléfono de una persona
#Ampliación:
#Al buscar a una persona, que te muestre todas aquellas que comiencen por el texto que has introducido. Ejemplo:
#Introduce un nombre: Pep
#Resultados:
#Pepe 659331013
#Pepe Martín 633743551
import logging
logging.basicConfig(level=logging.INFO)
class Consola:
    def __init__(self,lista):
        self.lista=lista
    def agregar_lista(self,persona):
        self.lista.append(persona)
        return self.lista    
    def mostrar_lista(self,lista,persona):
        if persona.name == lista[0]:
            return persona
        else:
            return persona
    def eliminar_persona(self, nombre, número):
        persona_encontrada = False
        for x in self.lista:
            if x.nombre == nombre and persona.número == número:
                self.lista.remove(x)
                persona_encontrada = True
                print("Se ha eliminado correctamente a "+nombre+" con número "+número+".")
                break
        if not persona_encontrada:
            print("No se ha encontrado a nadie con ese nombre y número.")
    def mostrar_persona(self, texto):
        resultados = []
        for persona in self.lista:
            if persona.nombre.startswith(texto):
                resultados.append(persona)
        return resultados

class Persona:
    def __init__(self,nombre,número):
        self.nombre=nombre
        self.número=número


lista=Consola([])

print("¡Bienvenido a la agenda de teléfonos!")
while True:
    print("¿Qué desea hacer?")
    print("Ingrese el número correspondiente a la operación que desea realizar:")
    print("1. Agregar persona a la agenda")
    print("2. Eliminar persona de la agenda")
    print("3. Ver agenda")
    print("4. Buscar persona de la agenda")
    print("5. Salir")
    operación = input("Operación que desea realizar: ")
    if operación == "1":
        print("Ha seleccionado la opción 1.")
        nombre=input("Ingrese el nombre de la persona que desee agregar: ")
        while True:
            if nombre.replace(" ","").isalpha() == True: #controlamos que sea letras o espacios
                break
            else:
                logging.error("ERROR. Solo se aceptan letras en el nombre.")
                nombre=input("Ingrese el nombre de la persona que desee agregar: ")
        nombre = nombre.title()
        número=input("Ingrese el número del usuario: ")
        while True:
            if número.isdigit() == True: #controlamos que sea números
                break
            else:
                logging.error("ERROR. Solo se aceptan números.")
                número=input("Ingrese el número del usuario: ")
        persona= Persona(nombre,número)
        lista.agregar_lista(persona)
    if operación == "2":
        print("Ha seleccionado la opción 2.")
        nombre_a_eliminar=input("Ingrese el nombre de la persona que desee eliminar: ")
        while True:
            if nombre_a_eliminar.replace(" ","").isalpha() == True: #controlamos que sea letras o espacios
                break
            else:
                logging.error("ERROR. Solo se aceptan letras en el nombre.")
                nombre_a_eliminar=input("Ingrese el nombre de la persona que desee eliminar: ")
        nombre_a_eliminar = nombre_a_eliminar.title()
        número_a_eliminar=input("Ingrese el número del usuario que desea eliminar: ")
        while True:
            if número_a_eliminar.isdigit() == True: #controlamos que sea números
                break
            else:
                logging.error("ERROR. Solo se aceptan números.")
                número_a_eliminar=input("Ingrese el número del usuario que desea eliminar: ")
        lista.eliminar_persona(nombre_a_eliminar,número_a_eliminar)
    if operación=="3":
        print("Ha seleccionado la opción 3.")
        print("Lista de empleados:")
        if len(lista.lista) > 0:    
            for x in lista.lista:
                print(f"Nombre: {x.nombre}, Número: {x.número}")
        else:
            print("No hay nadie en la lista.")
    if operación =="4":
        print("Usted ah elegido la opción 4.")
        texto=input("Ingrese el nombre de la persona que desee agregar: ")
        while True:
            if texto.replace(" ","").isalpha() == True: #controlamos que sea letras o espacios
                break
            else:
                logging.error("ERROR. Solo se aceptan letras en el nombre.")
                texto=input("Ingrese el nombre de la persona que desee agregar: ")
        texto = texto.title()
        resultado= lista.mostrar_persona(texto)
        if len(resultado) > 0:
            print("Resultados de la búsqueda:")
            for persona in resultado:
                print(f"Nombre: {persona.nombre}, Número: {persona.número}")
        else:
            print("No se encontraron resultados.")
    elif operación == "5":
        print("¡Gracias por su tiempo!")
        break
    else:
        logging.error("ERROR. Ingreso un carácter invalido,")    
    