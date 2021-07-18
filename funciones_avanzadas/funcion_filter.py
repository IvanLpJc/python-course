#Filtra resultados a partir de una lista y una condición

# Definimos la funcion condicional

def positivo(numero):
    if(numero>0):
        return True
    return False

numeros = [4,-1,8,-3,-5,-7,1,9]

# Primero pasamos la funcion filtro y luego la lista
filtro = filter(positivo, numeros)
print(list(filtro)) #[4, 8, 1, 9]