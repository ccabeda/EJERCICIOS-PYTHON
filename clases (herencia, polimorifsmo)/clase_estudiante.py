
#Crear una clase Persona con los atributos nombre, edad y dni. Luego, crear una clase hija llamada Estudiante, que herede de la clase Persona y 
#defina un atributo adicional código_estudiante. También, definir un método en la clase Estudiante llamado mostrar_información que imprima en pantalla 
#el nombre, edad, DNI y código de estudiante del estudiante.

class Persona:
    def __init__(self,nombre,edad,dni):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni

    def __str__(self):
        return "Soy una persona."

class Estudiante(Persona):
    def __init__(self, nombre, edad, dni,codigo_estudiante):
        super().__init__(nombre, edad, dni)
        self.codigo_estudiante = codigo_estudiante
    
    def mostrar_info(self):
        return "Hola, me llamo "+str(self.nombre)+" ,tengo "+str(self.edad)+" años. Mi dni es "+str(self.dni)+" y mi codigo estudiantil es "+str(self.codigo_estudiante)+"."

estudiante = Estudiante("Lucas",20,44419749,202020)
mostrar= estudiante.mostrar_info()
print (mostrar)