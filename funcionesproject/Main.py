base= int(input("Ingrese la base "))
altura= int(input("Ingrese la altura "))

#proceso
def calcularAreaTriangulo(a,b):
    area = (b*a)/2
    return area
#Invocar la funcion
resultado = calcularAreaTriangulo(base, altura)
print("El area del traiangulo es: ", resultado)

# Funcion con argumentos predeterminados
def my_function(country = "Colombia"):
    print("I am from "+ country)

#Invocar funcion
my_function()
my_function("Sweden")

#////////////////////
#Argumentos arbritarios
def mostrarEstudiantes(*args):
    print("El estudiante: " + args [2])

#Invocar la funcion
mostrarEstudiantes("Email","Tobias", "Linus", "Bill", "Andres")

#///////////////

def mostrarCarros(carro1,carro2,carro3):
    print ("El carro es: " +carro2)

mostrarCarros(carro1= "BMW", carro3= "Ferrari", carro2="Ford")

#///// Argumento **kwargs

def mostarCliente(**kwargs):
    print("Su apellido es: " + kwargs["telefono"])

mostarCliente(nombre= "Tobias", apellido = "Refsnes" , telefono = "123")

#///Declaracion de paso
def miFuncion():
 pass

#//////Funcionaes Integradas

x = min (5,10,25)
y = max (5,10,25)

print(x)
print(y)

num1 = pow(7 , 4)
print(num1)

#//////Modulo de matematicas
import math
num2=math.sqrt(34)

print(num2)

#//////
num3 = math.ceil(7.8)
num4= math.floor(7.8)

print(num3) #return 8
print(num4) #return 7