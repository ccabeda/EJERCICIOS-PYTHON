#Crea una clase llamada Rectángulo que tenga dos atributos: base y altura, y tres métodos:
#area() que devuelva el área del rectángulo.
#perímetro() que devuelva el perímetro del rectángulo.
#es_cuadrado() que devuelva True si el rectángulo es en realidad un cuadrado (es decir, si su base y altura son iguales), y False en caso contrario.
#Luego crea un objeto recto de la clase Rectángulo, donde le pases los valores de base y altura. Finalmente, muestra por pantalla el área, perímetro y si es cuadrado o no.

#creamos la clase con sus funciones y su constructor
class Rectángulo:
    def __init__ (self,base,altura):
        self.base=base
        self.altura=altura
    
    def area(self):
        area_total= self.base * self.altura
        return area_total
    
    def perímetro(self):
        perímetro_total= self.base*2 + self.altura *2
        return perímetro_total
    
    def es_cuadrado(self):
        if self.base == self.altura:
            return True
        else:
            return False
    #creamos la función que imprime 
    def __str__(self):
        return "El area del rectángulo es de "+str(self.area())+"cm, la altura de "+str(self.perímetro())+"cm. Es un cuadrado: "+str(self.es_cuadrado())

#pedimos los datos al usuario
base=input("Ingrese los centímetros de la base: ")
altura=input("Ingrese los centímetros de la altura: ")
#verificamos que sean dígitos a través de bucles
while True:
    if base.isdigit(): 
        break 
    else:
        print("Error. Debe ingresar dígitos unicamente") 
        base=input("Ingrese los centímetros de la base: ") 

while True:
    if altura.isdigit(): 
        break 
    else:
        print("Error. Debe ingresar dígitos unicamente") 
        altura=input("Ingrese los centímetros de la altura: ")
#creamos el objeto de la clase y los pasamos a int
rect= Rectángulo(int(base),int(altura))
print(rect)

