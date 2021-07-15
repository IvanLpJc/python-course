print("*********************************************")
print("*         Variables y numeros               *")
print("*********************************************")

numero = 5

print(numero)

cadena = "Hola mundo"
print(cadena)

# Las variables no pueden empezar por números
# 5numero = 5 -> esto da error

# Distingue entre mayusculas y minusculas
Numero = 0
numero = 3

print(Numero) # 0
print(numero) # 3

# Podemos concatenar cadenas utilizando el operador +

cadena1 = "Hola "
cadena2 = "mundo"
print(cadena1 + cadena2) # Hola mundo

numero1 = 5
numero2 = 4
print(numero1+numero2) # 9

# Podemos saber el tipo de una variable con type()
print(type(numero1)) #int
print(type(cadena1)) #string

# Podemos CONVERTIR el tipo de dato de una variable
numero = 5
cadena = str(numero)
print(cadena) # '5'
print(type(cadena)) #string

cadena = '25'
numero = int(cadena) 
print(numero) # 25
print(type(numero)) #int

cadena = '25.7'
numero = float(cadena)
print(type(numero)) #float

# Ejercicio 1: 
# Crear 'numero1' con el valor 5 e indicar su tipo 
# Crear 'numero2' con el valor 6.5 e indicar su tipo
# Crear 'numero3' con el valor 7 e indicar su tipo
# Crear 'suma' y que ocntenga la suma de los tres anteriores, 
# mostrar el resultado y el tipo
print("*********************************************")
print("               Ejercicio1                    ")
print("*********************************************")
numero1 = 5
print(type(numero1))
numero2 = 6.5
print(type(numero2))
numero3 = 5
print(type(numero3))

suma = numero1 + numero2 + numero3
print(suma)
print(type(suma))

# Ejercicio 2:
# Crear 'numero1' con el valor 5 
# Crear 'numero2' con el valor 3 
# Crear 'suma' y que ocntenga la suma de los dos anteriores
# COnvertir suma a cadena de caracteres y llamarla strSuma
# Crear una variable resultado que concatene "El resultado es" y la variable strSuma
print("*********************************************")
print("               Ejercicio2                    ")
print("*********************************************")
numero1 = 5
numero2 = 3
suma = numero1 + numero2
strSuma = str(suma)
resultado = "El resultado es {}".format(strSuma)
print(resultado)
