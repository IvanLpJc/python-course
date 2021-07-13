from typing import Sized


print("*********************************************")
print("*        Operadores aritmeticos             *")
print("*********************************************")

numero1 = 10
numero2 = 5
suma = numero2 + numero1

resta = numero1 - numero2

multiplicacion = numero1 * numero2

division = numero1 / numero2

numero3 = 3

resto = numero1 % numero3 # 1

cociente = numero1 // numero3 # 3

exponente = 2 ** 3 # 8

print("*********************************************")
print("*        Operadores de asignacion           *")
print("*********************************************")

numero = 5 

numero += 5 # 10

numero -= 2 # 8

numero *= 2 # 16

numero /= 4 # 4

numero **= 2 # 16

print("*********************************************")
print("*        Operadores de comparación          *")
print("*********************************************")

numero1 == numero2 # true si son iguales, false si no

cadena1 ="hola"
cadena2 ="hola"
cadena1 == cadena2 # true

if (cadena1 == "hola"):
    print("Dijo hola")

numero1 != numero2 #true si son distintos, false si son iguales

numero1 > numero2 # true si 1 es mayor que 2, false si no
numero1 < numero2 # true si 1 es menor que 2, false si no

numero1 >= numero2 # true si 1 es mayor o igual que 2, false si no
numero1 <= numero2 # true si 1 es menor o igual que 2, false si no

print("*********************************************")
print("*           Operadores lógicos              *")
print("*********************************************")

numero1 > numero2 and numero1 == numero #true si ambas condiciones se cumplen
numero1 > numero2 or numero1 == numero #true si una de las condiciones se cumple
not(numero1 > numero3) # si el interior es true, devuelve false, y viceversa

print("*********************************************")
print("*         Operadores de identidad           *")
print("*********************************************")

# Comprobamos si dos objetos son el mismo o no
frutas1 = ["manzana", "pera"]
frutas2 = ["manzana", "pera"]
frutas3 = frutas1

frutas3 is frutas1 # SOn el mismo objeto? En este caso si, devuelve true
frutas2 is frutas1 # NO son el mismo objeto, devuelve false
print(frutas1)
frutas3.append("naranja") # Como frutas3 y frutas1 son lo mismo, se añade a ambos

print(frutas3)
print(frutas1)

frutas1 is not frutas2 # devuelve true, porque son diferentes
frutas1 is not frutas3 # devuelve false, porque son el mismo

print("*********************************************")
print("*        Operadores de pertenencia          *")
print("*********************************************")

"manzana" in frutas1 # devuelve true, porque manzana está
"limon" in frutas1 # devuelve false, porque limon no está

"manzana" not in frutas1 # devuelve false, porque manzana está
"limon" not in frutas1 # devuelve true, porque limon no está

print("*********************************************")
print("*               Ejercicio 1                 *")
print("*********************************************")

# Crear "nota1" con el valor 6
# Crear "nota2" con el valor 4
# Crear "nota3" con el valor 7
# Crear "nota_media" con el valor medio de las tres notas
# Crear "Nota final" con el valor "aprobado" si es >= 5

nota1 = 6
nota2 = 4
nota3 = 7
nota_media = (nota1 + nota2 + nota3)/3
nota_final = "Aprobado" if nota_media >= 5 else "Suspenso"
print("El alumno está "+nota_final)

print("*********************************************")
print("*               Ejercicio 2                 *")
print("*********************************************")

# Crear "minimo" con el valor 20
# Crear "máximo" con el valor 500
# Recoger un valor por teclado y guardarlo en "dato"
# COnvertir "dato" a numero y guardarlo en "numero"
# Si "numero" es menor que "minimo", mostrar "valor bajo"
# Si "numero" es mayor que "maximo" mostrar "valor alto"
# Si está en el intervalo, mostrar "valor medio"

minimo = 20
maximo = 500

print("Introduce un número")
dato = input()
while(dato != 'q'):
    numero = float(dato)
    resultado = "Valor bajo" if numero < minimo else "Valor alto" if numero > maximo else "Valor medio"
    print(resultado)
    dato = input()

print("*********************************************")
print("*               Ejercicio 3                 *")
print("*********************************************")

# Crear "numeros" con una lista de numeros del 1 al 10
# Mostrar "numeros"
# Recoger dato por teclado y guardarlo en "dato"
# Convertir "dato" a numero y guardarlo en "numero"
# Si "numero" está en la lista, mostrar Si
# Si no está, mostrar No 

numeros = list(range(0,10))
print("Introduce un número")
dato = input()
while(dato != 'q'):
    n = float(dato)
    print("Si" if n in numeros else "No")
    dato = input()