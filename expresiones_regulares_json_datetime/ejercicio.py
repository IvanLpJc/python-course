
print("*********************************************")
print("                Ejercicio                    ")
print("*********************************************")

# Crear una funcion "buscar" que mediante una expresion regular indique si una palabra está en una frase

# Probar la función con:
#  - texto = "Esto es una frase de pruebas para hacer busquedas"
#  - palabra_a_buscar = "frase"

# Si se encuentra la palabra, indicar la posición en la que empieza y en la que finaliza
import re

def buscar(texto, palabra):
    resultado = re.search(palabra, texto)
    if(resultado):
        inicial = resultado.start()
        final = resultado.end()
        print(f"La palabra \"{palabra}\" está en la cadena y empieza en la posición {inicial} y termina en la posicion {final}")
    else:
        print("Cadena no encontrada")

texto = "Esto es una frase de pruebas para hacer busquedas"
palabra_a_buscar = "frase"

buscar(texto, palabra_a_buscar)