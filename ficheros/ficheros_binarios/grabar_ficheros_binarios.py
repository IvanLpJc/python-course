print("*********************************************")
print("        Ficheros binarios: Grabar            ")
print("*********************************************")

# pickle - Modulo para ficheros binarios
import pickle
import os

lista_colores = ['azul','verde','rojo','amarillo']

here = os.path.dirname(__file__)
filename = "fichero_colores.pckl" # Extension pickle para binarios
filepath = os.path.join(here, filename)

file = open(filepath, "wb") # b - binario

pickle.dump(lista_colores, file)

if(os.path.isfile(filepath)):
    print("Fichero binario creado")
    
file.close()