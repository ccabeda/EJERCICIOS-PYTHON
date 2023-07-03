#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
# #Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

#creamos la clase alumno
class Alumno:
    def __init__(self,nombre,nota):
        self.nota=nota
        self.nombre=nombre
#creamos la función de aprobado
    def aprobó(self):
        if self.nota >= 7:
            return self.nombre+" usted ah aprobado. Su nota es "+str(self.nota)
        else:
            return self.nombre+" usted ah desaprobado. Su nota es "+str(self.nota)

#variables para que ingresen los datos
nombre_alumno= input("Ingrese su nombre: ")
nota_alumno=input("Ingrese su nota: ")
#verificamos que la nota sea un dígito
while True: #ponemos True para que se ejecute si o si
    if nota_alumno.isdigit(): #mientras la nota sea un dígito
        break #rompemos el bucle porque ya es un dígito
    else:
        print("Error. Debe ingresar un dígito unicamente") #si no lo es, nos manda aca
        nota_alumno=input("Ingrese su nota: ") #para que no sea un bucle infinito
        
alumno=Alumno(nombre_alumno,int(nota_alumno)) #llamamos a la función con sus atributos, en este caso con el nombre de la variable. Ponemos int delante de nota ya que es un str
print(alumno.aprobó())