print("*********************************************")
print("*        Cadenas de caracteres              *")
print("*********************************************")
# Cadenas de caracteres
cadena = "Hola mundo"
print(cadena)

# H o l a   m u n d o
# 0 1 2 3 4 5 6 7 8 9
print(cadena[5]) # m
print(cadena[-1]) # o
print(cadena[2:7]) # la mu
print(cadena[2:]) # la mundo

# cadena[5] = 'p' -> no se puede hacer, son inmutables, 
# podemos acceder pero no podemos modificarlas

cadena1 = 'Hola'
cadena2 = 'mundo'
cadena3 = ' '

print(cadena1+cadena3+cadena2) # Hola mundo

print("*********************************************")
print("*         Funciones de cadenas              *")
print("*********************************************")

cadena = 'Hola mundo'
print(len(cadena)) # Muestra la longitud de la cadena -> 10
print(cadena.upper()) # Solo muestra la cadena en mayúsculas
cadena = cadena.upper() # Cambia la cadena a mayúsculas permanentemente
cadena = cadena.lower() # Cambia la cadena a minúsculas permanentemente
cadena.split() #devuelve una lista con las palabras de la cadena -> ['Hola' , 'mundo']
# Si a la función split le pasamos como parámetro un carácter, separará la cadena por 
# ese caracter.
cadena = 'uva,pera,manzana'
cadena.split(',') # ['uva', 'pera', 'manzana']

print("*********************************************")
print("*     Imprimir variables en cadenas         *")
print("*********************************************")

nombre = "Antonio"
print("Buenos días " + nombre)

# .format
edad = 18
print("Buenos días {}, feliz {} cumpleaños".format(nombre, edad)) # Buenos días Antonio, feliz 18 cumpleaños

# Si tenemos un número muy largo, por ejemplo, podemos formatearlo
resultado = 10/3 # 3.3333333333333335
print("El resultado es {r}".format(r=resultado)) # El resultado es 3.3333333333333335

print("El resultado es {r:1.3f}".format(r=resultado)) # {r:1.3f} significa 1 entero y 3 decimales
# El resultado es 3.333

# f-strings

print(f"Buenos días {nombre}, feliz {edad} cumpleaños")

print("*********************************************")
print("*         Entrada por teclado               *")
print("*********************************************")

print("Introduce un nombre")
entrada = input()
print("HOla " + entrada)

print("*********************************************")
print("               Ejercicio1                    ")
print("*********************************************")

# Crea la variable cadena con el texto "Esto es un texto de ejemplo"
# Según la posición de cada letra en la cadena, calcular que valores (x,y)
# hay que poner para seleccionar solo la palabra "texto"

cadena = "Esto es un texto de ejemplo"
print(cadena[11:16])

print("*********************************************")
print("               Ejercicio2                    ")
print("*********************************************")

# Crear "cadena" con "Esto es un texto de ejemplo"
# Crear "longitud" con la longitud de "cadena"
# Crear "strLongitud" con "longitud" pero siendo string
# Crear "mayusculas" con "cadena" en mayusculas
# Crear "resultado" con "mayusculas" concatenado con " tiene longitud de "
# y "strLongitud"

cadena = "Esto es un texto de ejemplo"
longitud = len(cadena)
strLongitud = str(longitud)
mayusculas = cadena.upper()
resultado = mayusculas + " tiene longitud de " + strLongitud
print(resultado)