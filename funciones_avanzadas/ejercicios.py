print("*********************************************")
print("                Ejercicio 1                  ")
print("*********************************************")
print(
    '''
    Crea la función primos que será una función generadora de primos entre el 0 y el 100
    Utiliza la función para mostrar los numeros primos menores de 50
    '''
)

def primos(max):
    for i in range(2,max):
        isPrime = True
        for j in range(2,i):
            if i%j == 0:
                isPrime = False
        if isPrime:
            yield i

print(
    '''
    Código solución:
    def primos(max):
        for i in range(2,max):
            isPrime = True
            for j in range(2,i):
                if i%j == 0:
                    isPrime = False
            if isPrime:
                yield i
    
    print(list(primos(50)))
    Resultado:
    '''
)


print(list(primos(50)))



print("*********************************************")
print("                Ejercicio 2                  ")
print("*********************************************")
print(
    '''
    A partir de una lista "numeros" que contiene los numeros del 1 al 10
    obtener mediante "filter" una lista denominada "pares" con los numeros pares
    '''
)

print(
    '''
    Código solución:
    numeros = list(range(1,11))

    print(list(filter((lambda x: x%2 == 0), numeros)))
    Resultado:
    '''
)
numeros = list(range(1,11))

print(list(filter((lambda x: x%2 == 0), numeros)))

print("*********************************************")
print("                Ejercicio 3                  ")
print("*********************************************")
print(
    '''
    Crea la función primos que será una función generadora de primos entre el 0 y el 100
    Obtener una nueva lista con todos los valores incrementados en 10
    '''
)
print(
    '''
    Códigoc solución:
    print(list(map((lambda x: x+10), numeros)))

    Resultado:
    '''
)
print(list(map((lambda x: x+10), numeros)))
