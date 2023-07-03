#Ejercicios de Herencia:
#Crear una clase Figura con los atributos base y altura y los métodos area y perímetro. Luego, crear dos clases hijas llamadas Triangulo y 
#Rectángulo, que hereden de la clase Figura y definir sus métodos area y perímetro.
import logging

class Figura:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area(self):
        return self.base*self.altura
    
    def perímetro(self):
        return self.base + self.altura
    
    def __str__(self):
        return "Soy una figura."

class Triangulo(Figura):
    def __init__(self, base, altura,lado1,lado2,lado3):
        super().__init__(base, altura)
        self.lado1 = lado1
        self.lado2=lado2
        self.lado3=lado3 
    
    def area(self):
        return (self.base*self.altura)/2
    
    def perímetro(self):
        return self.lado1 + self.lado2 + self.lado3 

    def __str__(self):
        return "Soy un triangulo."

class Rectángulo(Figura):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    
    def area(self):
        return (self.base*self.altura)
    
    def perímetro(self):
        return (self.base*2) + (self.altura*2) 

    def __str__(self):
        return "Soy un Rectángulo."

while True:
    print("Ingrese el número correspondiente a la figura que desee crear:")
    print("1. Rectángulo")
    print("2. Triangulo")
    operación=input("¿Que Figura quiere crear? ")
    
    if operación == "1":
        print ("¡Eligió el Rectángulo!")
        base = input("Ingrese los centímetros de la base: ")
        while True:
            if base.replace(".","").isdigit() == True: #controlamos que puedan ser números o enteros o flotantes
                break
            else:
                logging.error("ERROR. Solo se aceptan números.")
                base=input("Ingrese el salario del usuario: ")
        base= float(base)
        altura = input("Ingrese los centímetros de la altura: ")
        while True:
            if altura.replace(".","").isdigit() == True: #controlamos que puedan ser números o enteros o flotantes
                break
            else:
                logging.error("ERROR. Solo se aceptan números.")
                altura=input("Ingrese el salario del usuario: ")
        altura= float(base)
        rectángulo = Rectángulo(base,altura)
        print ("Creo un rectángulo de "+str(rectángulo.area())+"cm de área, y "+str(rectángulo.perímetro())+"cm de perímetro")
