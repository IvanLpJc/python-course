from typing import final


numero = 5
numero2 = 0

# division = numero / numero2   -> esto genera un error ZeroDivisionError

#Para controlar los errores utilizamos un try except
print("******* try except ***************")
try:
    division = numero / numero2
    print(division)
except: # Esto controla si hay un error y ejecuta el código siguiente
    print("Ha habido un error")

print("***** try except except **********")
# Si es un error en específico podemos controlarlo de otro modo
try:
    division = numero / numero2
    print(division)
except ZeroDivisionError:
    print("Error, divison por 0")
except: # Esto controla si hay un error y ejecuta el código siguiente
    print("Ha habido un error")

print("*** try except except else *******")
#Si no hay error, podemos usar un else
try:
    numero3 = 2
    #division = numero / numero2
    division = numero / numero3
    print(division)
except ZeroDivisionError:
    print("Error, divison por 0")
except: # Esto controla si hay un error y ejecuta el código siguiente
    print("Ha habido un error")
else: # Si no hay errores ejecuta esto tras el bloque try
    print("La division funcionó correctamente")

# Con finally podemos ejecutar código sin importar el resultado del try except
print("* try except except else finally **")
try:
    numero3 = 2
    #division = numero / numero2
    division = numero / numero3
    print(division)
except ZeroDivisionError:
    print("Error, divison por 0")
except: # Esto controla si hay un error y ejecuta el código siguiente
    print("Ha habido un error")
else: # Si no hay errores ejecuta esto tras el bloque try
    print("La division funcionó correctamente")
finally:
    print("Esta prueba se ha acabo")

print("*********************************************")
print("       Gestión de errores: Ejercicio         ")
print("*********************************************")

# Crear funcion operacion que dados 3 numeros divida el primero entre la resta de los otros 2
# Usar la funcion con los numeros 5,4,2
# Usar la funcion con los numeros 6,3,3

# Usar try except para controlar errores

def operacion(n1,n2,n3):
    try:
        divisor = n2-n3
        division = n1 / divisor
        print(f"{n1}/({n2}-{n3}) = {division}")
    except ZeroDivisionError:
        print(f"Error, division por 0: {n2}-{n3} = {divisor}")
    except:
        print("Error en la operacion")
    else:
        print("Ejecución realizada con éxito")
        print("*******************************")
operacion(5,4,2)
operacion(6,3,3)