# Son funciones que generan valores "sobre la marcha"

range(0,11)  # Genera valores desde 0 a 10, es lo mismo que decir range(11)

for numero in range(0,11):
    print(numero)

print("*************************************")

def pares(maximo):
    for numero in range(maximo):
        if(numero % 2 == 0):
            yield numero

# En lugar de return, utilizamos yield, que no detiene la ejecución
# en este caso suelta un numero par cada vez que lo encuentra

for numero in pares(11):
    print(numero)