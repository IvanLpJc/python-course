#Leer el fichero de texto
# Por alguna razón no encuentra el fichero al hacer simplemente
# open("fichero_texto.txt") por lo que hay que importar el modulo os
# extraer el path hasta donde está este archivo .py
# añadir el nombre del fichero al path
# usar ese path para abrir el fichero

import os
here = os.path.dirname(__file__)
filename = "fichero_texto.txt"
filepath = os.path.join(here, filename)
fichero = open(filepath, "rt") # Abrimos el fichero en modo lectura y modo texto (no es una imagen)

datos_fichero = fichero.read() # Lee el contenido del fichero y lo guarda
print(datos_fichero)

fichero.close()