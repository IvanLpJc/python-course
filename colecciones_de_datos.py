print("*********************************************")
print("*                Listas                     *")
print("*********************************************")

# Colección de elementos ordenada y modificable

colores = ["rojo", "amarillo", "verde"]
print(colores) 
colores[0] # 'rojo'
colores[1] # amarillo

colores[1] = "azul" # ["rojo", "azul", "verde"]

len(colores) # 3

colores.append("naranja") # ["rojo", "amarillo", "verde", "naranja"]
print(colores) 
colores.remove("rojo") # ["amarillo", "verde", "naranja"]
print(colores) 
for color in colores:
    print(color) # Imprime cada color de colores uno a uno

colores.clear() # limpia la lista
print(colores) # []
print("*********************************************")
print("*                Tuplas                     *")
print("*********************************************")

# Colección de elementos ordenada no modificable

tupla_colores = ("rojo", "amarillo", "verde")

print(tupla_colores) # ("rojo", "amarillo", "verde")

for color in tupla_colores:
    print(color)

print(tupla_colores[2]) # amarillo

print(len(tupla_colores)) # 3

print("*********************************************")
print("*              Conjuntos                    *")
print("*********************************************")

# Colección de elementos desordenado

conjunto_colores = {"rojo", "amarillo", "verde"}
print(conjunto_colores) # {"rojo", "amarillo", "verde"}

for color in conjunto_colores:
    print(color)

# No soporta indexación -> conjunto_colores[0] no funciona
print(len(conjunto_colores))

conjunto_colores.add("negro")
print(conjunto_colores) # {"rojo", "negro" "amarillo", "verde"}
conjunto_colores.remove("verde") # {"rojo", "amarillo", "negro"}

print("*********************************************")
print("*             Diccionarios                  *")
print("*********************************************")

# Colección de elementos que están indexados, no ordenados y modificables

diccionario_colores = {"red":"rojo", "blue":"azul", "yellow":"amarillo"}
print(diccionario_colores)

diccionario_colores["red"] # 'rojo'

diccionario_colores["black"] = "negro" # Añade la clave black con el valor negro
                                    # 'red': 'rojo', 'blue': 'azul', 'yellow': 'amarillo', 'black': 'negro'}
diccionario_colores.pop("yellow") # Borramos yellow -> {'red': 'rojo', 'blue': 'azul', 'black': 'negro'}

del(diccionario_colores['black']) # elimina el elemento black -> {'red': 'rojo', 'blue': 'azul'}

for color in diccionario_colores:
    print(color) # imprime las claves

for key, value in diccionario_colores.items():
    print(key, value) # imprime las claves y los valores

print("*********************************************")
print("*             Ejercicio 1                   *")
print("*********************************************")

# Dada la lista [1,2,5,25,33,56,75,21,56,89,43,13,62,24]
# Muestra si el numero 21 está en la lista

lista = [1,2,5,25,33,56,75,21,56,89,43,13,62,24]
if( 21 in lista):
    print("21 está en la lista")

print("*********************************************")
print("*             Ejercicio 2                   *")
print("*********************************************")

# Crea una tupla con los nombres Antonio, Pedro y María
# MOstrar la tupla
# Recoger un valor por teclado en "dato"
# Si "dato" está en la tupla, mostrar Si
# Si no, mostrar No 

nombres = ("Antonio", "Pedro", "María")
print(nombres)
dato = input()

print("Si" if dato in nombres else "No")

print("*********************************************")
print("*             Ejercicio 3                   *")
print("*********************************************")

# Crea un conjunto con los valores 1 a 5
# Mostrar conjunto
# Añadir del 6 al 9 al conjunto 
# MOstrar conjunto 
# Eliminar el 9
# Mostrar el conjunto
# Verificar el tipo de conjunto con type

conjunto = set(range(5))
print(conjunto)
for i in range(6,10):
    conjunto.add(i)
print(conjunto)
conjunto.remove(9)
print(conjunto)
print(type(conjunto))

print("*********************************************")
print("*             Ejercicio 4                   *")
print("*********************************************")

# Crea un diccionaro con:
#     uno -> one 
#     dos -> two 
#     tres -> three
# Muestra por pantalla el diccionario
# Añadir cuatro -> four 
# Mostrar el diccionario
# Recoger un valor por teclado y guardaro en dato
# Usar dato para obtener su valor

diccionario = {'uno':'one', 'dos':'two','three':'tres'}
print(diccionario)
diccionario['cuatro'] = 'four'
print(diccionario)
dato = input()
print(diccionario[dato] if dato in diccionario else "No hay valor para esa clave")
