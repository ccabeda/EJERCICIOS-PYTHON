#Crea una clase Persona con las siguientes variables:
#La edad
#El nombre
#El teléfono
#Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la variable crédito solo para esa clase.
#Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el teléfono, el nombre y el crédito, tienes que darles valor y mostrarlas por pantalla.
#Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable


class Persona:
    def __init__(self,nombre,edad,teléfono):
        self.nombre=nombre
        self.edad=edad
        self.teléfono=teléfono
    
    def __str__(self):
        return "Soy "+str(self.nombre)+", tengo "+str(self.edad)+" años. Mi numero es "+str(self.teléfono)+". "

class Cliente(Persona):
    def __init__(self, nombre, edad, teléfono,crédito):
        super().__init__(nombre, edad, teléfono)
        self.crédito=crédito
    def __str__(self) -> str:
        return super().__str__() + "Ademas, soy un cliente. Mi crédito es: "+str(self.crédito)
    
class Trabajador(Persona):
    def __init__(self, nombre, edad, teléfono, sueldo):
        super().__init__(nombre, edad, teléfono)
        self.sueldo=sueldo
    def __str__(self) -> str:
        return super().__str__() + "Ademas, soy un trabajador. Mi sueldo es de: "+str(self.sueldo)+"$ dólares."

cliente = Cliente("Juan",22,1144573628,20.000)
trabajador= Trabajador ("José",35,1138907356,90000)
print(cliente)
print (trabajador)