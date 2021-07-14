print("*********************************************")
print("        Ficheros binarios: Leer              ")
print("*********************************************")

import pickle
import os

here = os.path.dirname(__file__)
filename = "fichero_colores.pckl"
filepath = os.path.join(here, filename)

file = open(filepath, "rb")

data = pickle.load(file)

print(data)

file.close()
