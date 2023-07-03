#Para practicar la encapsulación:
#Crear clase Persona.
#Crear variables las privadas edad, nombre y teléfono de la clase Persona.
#Crear gets y sets de cada propiedad.
#Crear un objeto persona en el main.
#Utiliza los gets y sets para darle valores a las propiedades edad, nombre y teléfono, por último muéstralas por consola.

#! creamos la clase con los atributos en privado gracias al _
class Persona:
    def __init__(self):
        self._edad= 0 #!edad privada
        self._nombre= ""
        self._teléfono= 0
#!creamos los métodos que reciben (set) y devuelven (get) el atributo
    def get_edad(self):
        return self._edad
    
    def set_edad(self, edad):
        self._edad = edad
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre    
    
    def get_teléfono(self):
        return self._teléfono
    
    def set_teléfono(self, teléfono):
        self._teléfono = teléfono
#! creamos el objeto de la clase persona
persona = Persona()
#!le agregamos los datos con el set
persona.set_edad(20)
persona.set_nombre("Agustín")
persona.set_teléfono(1138907457)
#! los mostramos por pantalla con el get
print("Hola, mi nombre es "+str(persona.get_nombre()))