#Primera parte:
#Crear una función con tres parámetros que sean números que se suman entre sí.
#Llamar a la función en el main y darle valores.
#Segunda parte:
#Crear una clase coche.
#Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
#Una función que incremente el número de puertas que tiene el coche.
#Crear un objeto miCoche en el main y añadirle una puerta.
#Mostrar el número de puertas que tiene el objeto.

def suma_entre_si(*números):
    return sum(números)

resultado= suma_entre_si(9,8,7,6,5,4,3,2,1)
print(resultado)

class Coche:
    def __init__(self,puertas):
        self.puertas=puertas

    def incrementar_puertas(self,aumento):
        nuevas_puertas= self.puertas + aumento
        return nuevas_puertas
    
    def __str__(self):
        return "Hola, soy un coche de "+str(self.puertas)+" puertas."

mi_coche= Coche(4)
print(mi_coche)

nuevo_coche = mi_coche.incrementar_puertas(3)
print("Hola, soy un coche de "+str(nuevo_coche)+" puertas.")
