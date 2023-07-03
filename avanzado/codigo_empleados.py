#Crea una clase GestorEmpleados que permita gestionar la información de una lista de empleados. La clase debe tener los siguientes métodos:
#agregar_empleado(empleado): agrega un objeto de la clase Empleado a la lista de empleados.
#eliminar_empleado(empleado): elimina un objeto de la clase Empleado de la lista de empleados.
#obtener_salario_total(): devuelve la suma de los salarios de todos los empleados de la lista.
#obtener_empleado_mas_antiguo(): devuelve el objeto de la clase Empleado que lleva más tiempo en la empresa.
#obtener_promedio_edad(): devuelve el promedio de edad de los empleados de la lista.
#La clase Empleado debe tener los siguientes atributos:
#nombre: el nombre del empleado.
#edad: la edad del empleado.
#salario: el salario del empleado.
#fecha_ingreso: la fecha en que el empleado ingresó a la empresa.
#Además, la clase Empleado debe tener un método obtener_antigüedad() que devuelve el número de años que el empleado lleva en la empresa.

#importamos
import datetime
from functools import reduce
import logging
logging.basicConfig(level=logging.INFO)
#creamos clase
class Empleado:
    #sus atributos
    def __init__(self,nombre,dni,edad,salario,fecha_ingreso):
        self.nombre = nombre
        self.dni=dni
        self.edad = edad
        self.salario = salario
        self.fecha_ingreso = fecha_ingreso
    #función
    def obtener_antiguedad(self):
        hoy = datetime.datetime.today()
        antiguedad = hoy.year - self.fecha_ingreso.year
        if (hoy.month, hoy.day) < (self.fecha_ingreso.month, self.fecha_ingreso.day):
            antiguedad -= 1
        return antiguedad
#clase gestor que es una lista
class GestorEmpleado:
    #atributos
    def __init__(self,lista_empleados):
        self.lista_empleados = lista_empleados
    #funciones
    def agregar_empleado(self,empleado):
        self.lista_empleados.append(empleado)

    def eliminar_empleado(self,dni):
        for x in self.lista_empleados:
            if x.dni == dni:
                self.lista_empleados.remove(x)
                print("Empleado eliminado correctamente.")
            else:
                print("No se encontró un usuario con ese DNI.")

    def obtener_salario_total(self):
        salario_total = 0
        for x in self.lista_empleados:
            salario_total = salario_total + x.salario
        return salario_total

    def obtener_mas_antiguo(self):
        mas_antiguo = self.lista_empleados[0]
        for x in self.lista_empleados:
            if x.fecha_ingreso < mas_antiguo.fecha_ingreso:
                mas_antiguo= x.nombre 
        return mas_antiguo

    def promedio_edad(self):
        cantidad_empleados = len(self.lista_empleados)
        total_edad= 0
        for x in self.lista_empleados:
            total_edad = total_edad + x.edad
        return total_edad/cantidad_empleados

gestor= GestorEmpleado([]) #creamos un objeto de la clase gestor
#hacemos el menú
print("¡Bienvenido! ¿Que desea hacer hoy?")
while True:
    print("Ingrese el número correspondiente a la operación que desea realizar:")
    print("1. Agregar empleado a la lista")
    print("2. eliminar empleado de la lista")
    print("3. Obtener antigüedad de un empleado")
    print("4. Obtener el salario total")
    print("5. Obtener la edad promedio")
    print("6. Ver lista de empleados")
    print ("7. Salir")
    operación=input("Operación que desea realizar: ")
    if operación == "1":
        # Acciones correspondientes a la opción 1
        print("Ha seleccionado la opción 1.")
        nombre=input("Ingrese el nombre del empleado: ")
        while True:
            if nombre.replace(" ","").isalpha() == True: #controlamos que sea letras o espacios
                break
            else:
                logging.error("ERROR. Solo se aceptan letras en el nombre.")
                nombre=input("Ingrese el nombre del empleado: ")
        nombre = nombre.title()
        dni=input("Ingrese el dni del usuario: ")
        while True:
            if dni.isdigit() == True: #controlamos que sea números
                break
            else:
                logging.error("ERROR. Solo se aceptan números.")
                dni=input("Ingrese el dni del usuario: ")         
        edad=input("Ingrese la edad del empleado: ")
        while True:
            if edad.isdigit() == True: #controlamos que sean números
                break
            else:
                logging.error("ERROR. Solo se aceptan números.")
                edad=input("Ingrese la edad del usuario: ")
        edad = int(edad)
        salario=input("Ingrese el salario del empleado: ")
        while True:
            if salario.replace(".","").isdigit() == True: #controlamos que puedan ser números o enteros o flotantes
                break
            else:
                logging.error("ERROR. Solo se aceptan números.")
                salario=input("Ingrese el salario del usuario: ")
        salario= float(salario)
        fecha_ingreso = datetime.datetime.today()
        empleado = Empleado(nombre,dni,edad,salario,fecha_ingreso) #creamos objeto de la clase empleado
        gestor.agregar_empleado(empleado)
        print("Empleado agregado correctamente")
    elif operación == "2":
        # Acciones correspondientes a la opción 2
        print("Ha seleccionado la opción 2.")
        dni_a_eliminar= input("Ingrese el DNI del usuario que desea eliminar: ") #buscamos dni de la persona que queremos sacar
        while True:
            if dni_a_eliminar.isdigit() == True: #que sea solo números
                break
            else:
                logging.error("ERROR. Solo se aceptan números.")
                dni_a_eliminar=input("Ingrese el DNI del usuario que desea eliminar: ") 
        gestor.eliminar_empleado(dni_a_eliminar) #eliminamos
    elif operación == "3":
        # Acciones correspondientes a la opción 3
        print("Ha seleccionado la opción 3.")
        ver_antiguedad = input("Ingrese el DNI de la persona que desea ver su antiguedad: ") #buscamos dni de la persona que queremos 
        while True:
            if ver_antiguedad.isdigit() == True: #que sea número
                break
            else:
                logging.error("ERROR. Solo se aceptan números.")
                ver_antiguedad=input("Ingrese el DNI del usuario que desea eliminar: ") 
        encontrado = False #verificamos si el dni existe o no hay nadie registrado
        for x in gestor.lista_empleados:
            if ver_antiguedad == x.dni:
                ver_antiguedad = x.obtener_antiguedad()
                print("La antiguedad del empleado "+str(x.nombre)+" es de "+str(ver_antiguedad)+" años.")
                encontrado = True #si existe, se hace true
        if  encontrado == False: #sino sigue false
            print("No se encontró al usuario de ese DNI.")
    elif operación == "4":
        # Acciones correspondientes a la opción 4
        print("Ha seleccionado la opción 4.")
        salario_total = gestor.obtener_salario_total() #calculamos salario total
        print("El salario total es de "+str(salario_total)+"$") 
    elif operación == "5":
        # Acciones correspondientes a la opción 5
        print("Ha seleccionado la opción 5.")
        edad_promedio= gestor.promedio_edad() #calculamos edad promedio
        print("La edad promedio es de "+str(edad_promedio)+" años.")
    elif operación == "6":
        #Acciones correspondientes a la opción 6
        print("Ha seleccionado la opción 6.")
        if len(gestor.lista_empleados) > 0: #si hay mas de 0 personas
            print("Lista de empleados:")
            for empleado in gestor.lista_empleados: #que lea la lista e imprima sus empleados
                print(f"Nombre: {empleado.nombre}, DNI: {empleado.dni}, Edad: {empleado.edad}, Salario: {empleado.salario}, Fecha de ingreso: {empleado.fecha_ingreso}")
        else:
            print("No hay empleados en la lista.") #si no hay mas de 0, imprime esto
    elif operación == "7":
        print("¡Gracias por su tiempo!")
        break
    else:
        logging.error("ERROR. Ingreso un carácter invalido,")



