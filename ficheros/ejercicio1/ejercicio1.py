print("*********************************************")
print("               Ejercicio1                    ")
print("*********************************************")

#Crear el módulo "moduloficheros.py"
#   Crear la clase Fichero
#   Crear la función "leer_fichero" 
#   Crear la función "grabar_fichero" para crear un fichero
#   Crear la función "incluir_fichero" para incluir datos al final

#Crear un programa "ejericicio1.py"
#   Crear un objeto "fichero" de la clase "Fichero" 
#   Utilizar el método "grabar_fichero" para crear un nuevo fichero
#   Utilizar el metodo "incluir_fichero" para incorporar más datos
#   Utilizar el metodo "leer_fichero" para ver todo el contenido

from os import path
import moduloficheros

fichero = moduloficheros.Fichero()
base_path = "nuevo_fichero"
sufix = ".txt"
filename = base_path+sufix
if(fichero.fichero_existe(filename)):
    for i in range(100):
        filename = base_path + str(i) + sufix
        if(not fichero.fichero_existe(filename)):
            break


fichero.grabar_fichero(filename)

print(f"********* Contenido del {filename} ***********")
print(fichero.leer_fichero(filename))

fichero.incluir_fichero(filename)

print(f"********* Contenido de {filename} ************")
print(fichero.leer_fichero(filename))