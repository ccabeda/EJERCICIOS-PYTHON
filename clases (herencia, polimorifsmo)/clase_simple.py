#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos: Color, Ruedas, Puertas
#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos: Velocidad, Cilindrada
#Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

#creamos la clase vehículo, donde usamos def __init__ ya que queremos que los atributos los añadan por la terminal
class Vehículo:
    def __init__(self,color,ruedas,puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas
#creamos la otra clase
class Chevrolet_Cruz(Vehículo):
    def __init__(self,velocidad,cilindrada):
        #aca definimos el constructor heredado, que necesita los valores de los atributos de la case base
        super().__init__("Rojo",4,4)
        self.cilindrada=cilindrada
        self.velocidad=velocidad
    #esto es una función que permite devolver un string simplemente llamando la función, sin necesidad de por ejemplo: print(coche.datos())    
    def hola(self):
        return f"Coche de color {self.color}, {self.ruedas} ruedas, {self.puertas} puertas, {self.velocidad} km/h de velocidad y {self.cilindrada} cc de cilindrada."
#creamos un objeto de la variable
coche= Chevrolet_Cruz(9,12)
print(coche)
