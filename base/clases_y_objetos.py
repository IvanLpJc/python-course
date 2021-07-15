print("*********************************************")
print("*            Clases y objetos               *")
print("*********************************************")

class claseSilla:
    color = "blanco"
    precio = 100

silla = claseSilla()
print(silla.color)
print(silla.precio)

silla2 = claseSilla()
silla2.color = "verde"
silla2.precio = 120


print(silla2.color)
print(silla2.precio)

class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

persona = Persona("Juan", 37)
persona.saludar()

print("*********************************************")
print("*                Funciones                  *")
print("*********************************************")

def saludo(nombre):
    print("Buenos días " + nombre)

saludo("Pepe")

def suma(n1,n2):
    return n1+n2

print(suma(5,8))

# Paso de valor por referencia

colores = ['rojo','verde','azul']

def incluir_color(colores, color):
    colores.append(color) #incluye el color nuevo en colores


incluir_color(colores, "negro")
print(colores)

print("*********************************************")
print("*            Funciones lambda               *")
print("*********************************************")

# FUncion pequeña y anonima

resultado = lambda numero: numero + 30 # La función recibe un número y le suma 30, devolviendo el resultado

print(resultado(10)) # A la función lambda se le llamaría así, devolviendo 40

resultado2 = lambda n1, n2: n1+n2
print(resultado2(5,8))

print("*********************************************")
print("*             Ejercicio 1                   *")
print("*********************************************")

# Crear clase Coche con los atributos marca, color, combustible y cilindrada
# Crear la función __init__ que asigne los parametros de la clase a los atributos
# Crear la función mostrar_características usando print para mostrar los atributos
# Crear un objeto coche1 con los atributos opel rojo gasolina y 1.6
# Ejecutar mostrar_caracteristicas

class Coche:
    def __init__(self, marca, color, combustible, cilindrada) -> None:
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrar_características(self):
        print(f"El coche es un {self.marca}, de color {self.color}, utiliza {self.combustible} y tiene un motor de {self.cilindrada} litros")

coche1 = Coche("Opel", "rojo", "gasolina", '1.6')

coche1.mostrar_características()
print("*********************************************")
print("*             Ejercicio 2                   *")
print("*********************************************")

# Crea una funcion lambda que calcule la media de tres notas

media = lambda n1,n2,n3: (n1+n2+n3)/3

print(media(5,7,2))