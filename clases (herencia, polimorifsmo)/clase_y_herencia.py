#Supongamos que queremos crear una clase "Animal" que tenga las características comunes a todos los animales, y 
#luego queremos crear dos subclases "Perro" y "Gato" que hereden esas características y tengan algunas propias.

#creamos la clase animal
class Animal:
    def __init__(self,edad,nombre):
        self.edad=edad
        self.nombre=nombre
    #creamos sus funciones    
    def hablar(self):
        return "Hola a todos, estoy hablando!"
    
    def jugar(self):
        return "Estoy jugando"
    
    def __str__(self):
        return "Hola, soy "+str(self.nombre)+" y mi edad es "+str(self.edad)+" años."
#clase perro
class Perro(Animal):
    def __init__(self, edad, nombre,raza):
        super().__init__(edad,nombre)
        self.raza=raza
    #funciones de la clase perro
    def hablar(self):
        return "Guau"
    
    def __str__(self):
        return super().__str__() + "Soy un "+str(self.raza)+"."
    
#clase gato
class Gato(Animal):
    def __init__(self, edad, nombre,color):
        super().__init__(edad,nombre)
        self.color=color
    #funciones de la clase gato
    def hablar(self):
        return "Miau"
    
    def __str__(self):
        return super().__str__() + "Soy de color "+str(self.color)+"."
#función para que la edad sea un número
def validar_edad():
    while True:
        edad = input("Ingrese la edad de la mascota: ")
        if edad.isdigit():
            return edad
        else:
            print("Por favor, seleccione números para marcar la edad.") 
            
#pedimos los datos
nombre_animal= input("Ingrese el nombre de su animal: ")
edad_animal= validar_edad()
#creamos un objeto
animal = Animal(edad_animal,nombre_animal)  
print(animal)
print(animal.jugar())
print(animal.hablar())

nombre_perro= input("Ingrese el nombre de su perro: ")
edad_perro= validar_edad()
raza_perro=input("Ingrese la raza del perro: ")

perro= Perro(edad_perro,nombre_perro,raza_perro)
print(perro)
print(perro.jugar())
print(perro.hablar())

nombre_gato= input("Ingrese el nombre de su gato: ")
edad_gato= validar_edad()
color_gato=input("Ingrese el color del gato: ")

gato= Gato(edad_gato,nombre_gato,color_gato)
print(gato)
print(gato.jugar())
print(gato.hablar())

