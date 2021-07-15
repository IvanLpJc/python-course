print("*********************************************")
print("*          Bucles y condiciones             *")
print("*********************************************")

print("*********************************************")
print("*        Condicional if elif else           *")
print("*********************************************")

a = 8 
b = 4

if(a > b):
    print("a>b")
elif (a == b):
    print("a = b")
else:
    print("a < b")

print("*********************************************")
print("*                Bucle for                  *")
print("*********************************************")

colores = ["rojo", "amarillo", "verde"]
for color in colores:
    print(color)

cadena = "Hola mundo"
for caracter in cadena:
    print(caracter)

print("---------------")
for numero in range(8): # del 0 al 8
    print(numero)

print("---------------")
for numero in range(3,8): #del 3 al 8
    print(numero)
print("---------------")
for numero in range(3,8,2): #del 3 al 8 saltando de dos en dos
    print(numero)
print("---------------")

#break - detiene el bucle

for n in range(10):
    if(n == 5):
        break # deja de ejecutar el bucle al llegar al 5
    print(n)

print("---------------")

# continue - se salta la interaccion pero sigue el bucle
for n in range(10):
    if(n == 5):
        continue # no imprime el numero 5
    print(n)

print("---------------")

for n1 in range(4):
    for n2 in range(3):
        print(n1,n2)


print("*********************************************")
print("*                Bucle while                *")
print("*********************************************")

valor =1
fin = 10
while(valor < fin):
    print(valor)
    valor+=1
print("---------------")
valor =1
while(valor < fin):
    print(valor)
    valor+=1
    if(valor == 5):
        break #para el bucle al llegar a 5

print("---------------")
valor = 1
while(valor < fin):
    valor+=1
    if(valor == 5):
        continue # se salta el 5
    print(valor)

print("*********************************************")
print("*                Ejercicio 1                *")
print("*********************************************")

# Crea un diccionario con:
#     manzana, apple
#     naranja, orange
#     platano, banana
#     limon, lemon

# Muestra la traducción de naranja
# añade un elemento nuevo con piña y pineapple
# Muestra todo los elementos con un bucle

diccionario = {'manzana':'apple','naranja':'orange', 'platano':'banana', 'limon':'lemon'}

print(diccionario['naranja'])
diccionario['piña'] = 'pineapple'
for key, value in diccionario.items():
    print(key, value)

print("*********************************************")
print("*                Ejercicio 2                *")
print("*********************************************")

# Crear nota con el valor 4.5
# Crear trabajo_realizado con el valor "si"
# Calcular nota_final teniendo en cuenta que, si nota_final es >= a 4 y el valor de 
# trabajo_realizado es "si", entonces nota_final == "aprobado" si no, "suspenso"

nota = 4.5
trabajo_realizado = "Si"

nota_final = "Aprobado" if trabajo_realizado == "Si" and nota > 4 else "suspenso"
print(nota_final)


