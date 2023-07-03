#Crear una función llamada calcular_area que acepte un objeto de cualquier tipo que tenga un método llamado area. La función debe llamar al método area del objeto y 
#devolver el resultado. Luego, crear una clase Circulo con un método area que calcule el área del círculo. Finalmente, crear un objeto de la clase Circulo y 
#pasar ese objeto a la función calcular_area.
#Crear una clase Animal con un método llamado hacer_ruido que imprima en pantalla el sonido que hace el animal. Luego, crear dos clases hijas llamadas Perro y 
#Gato, que hereden de la clase Animal y definir sus métodos hacer_ruido. Por último, crear una lista de objetos que incluya un objeto de la clase Perro y un 
#objeto de la clase Gato y recorrer la lista llamando al método hacer_ruido de cada objeto."""

# Definir la función calcular_area que acepte cualquier objeto con un método area
def calcular_area(objeto):
    return objeto.area()

# Definir la clase Circulo con un método area que calcule el área del círculo
class Circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return 3.14 * self.radio ** 2

# Crear un objeto de la clase Circulo y pasarlo a la función calcular_area
mi_circulo = Circulo(5)
print(calcular_area(mi_circulo)) # salida: 78.5

# Definir la clase Animal con un método hacer_ruido que imprima en pantalla el sonido que hace el animal
class Animal:
    def hacer_ruido(self):
        print("Soy un animal y hago ruido.")

# Definir las clases hijas Perro y Gato con métodos hacer_ruido diferentes
class Perro(Animal):
    def hacer_ruido(self):
        print("Guau! Soy un perro.")

class Gato(Animal):
    def hacer_ruido(self):
        print("Miau! Soy un gato.")

# Crear una lista de objetos que incluya un objeto de la clase Perro y un objeto de la clase Gato
mis_animales = [Perro(), Gato()]

# Recorrer la lista y llamar al método hacer_ruido de cada objeto
for animal in mis_animales:
    animal.hacer_ruido()