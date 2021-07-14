print("*********************************************")
print("       Ficheros binarios: Ejercicio          ")
print("*********************************************")

# Crear diccionario "Frutas"
# frutas = {"manzana":"apple", "naranja":"orange", "platano":"banana", "limon":"lemon"}

# Grabar el diccionario en un fichero "fichero.pckl"
# Al ser un fichero de texto, solo seguardan caracteres, no estructuras

# Recuperar los datos del fichero 
# Comprobar que es un diccionario usando .values()


import pickle
import os

here = os.path.dirname(__file__)
filename = "fichero.pckl" # Extension pickle para binarios
filepath = os.path.join(here, filename)
file = open(filepath, "wb")

frutas = {"manzana":"apple", "naranja":"orange", "platano":"banana", "limon":"lemon"}

pickle.dump(frutas,file)
file.close()
file = open(filepath, 'rb')
data = pickle.load(file)

print(data.values())

file.close()