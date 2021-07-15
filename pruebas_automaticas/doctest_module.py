# Generación de pruebas automáticas dentro de la documentación

def suma(numero1, numero2):
    #Podemos poner todos los tests que queramos
    """
    Esto es la documentación de esta función
    Recibe dos números como parámetros y devuelve su suma
    >>> suma(4,3)
    7
    >>> suma(5,5)
    10
    >>> suma(10,2)
    12

    """
    
    return numero1 + numero2

resultado = suma(2,4)

print(resultado)

# Para que nos ejecute la prueba dentro del comentario
# tenemos que importar el modulo doctest y llamar al 
# metodo testmod

# Después, ejecutamos con la opción -v
import doctest
doctest.testmod()
# Nos imprime por pantalla con solo un test:

# Trying:
#     suma(4,3)
# Expecting:
#     7
# ok
# 1 items had no tests:
#     __main__
# 1 items passed all tests:
#    1 tests in __main__.suma
# 1 tests in 2 items.
# 1 passed and 0 failed.
# Test passed.