# Sirve para aplicar una función a una lista

def multiplicar(numero):
    return numero*2

numeros = [4,-1,8,-3,-5,-7,1,9]

mapeo = map(multiplicar, numeros)

print(list(mapeo)) # [8, -2, 16, -6, -10, -14, 2, 18]

# Se puede hacer todo en la misma linea

print(list(map(multiplicar, numeros))) # [8, -2, 16, -6, -10, -14, 2, 18]

# Podemos usar una función lambda
print(list(map(lambda x: x*2, numeros))) # [8, -2, 16, -6, -10, -14, 2, 18]