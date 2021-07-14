import os
here = os.path.dirname(__file__)
filename = "fichero_para_incluir_datos.txt"
filepath = os.path.join(here, filename)
fichero = open(filepath, "at") # a - append (añadir) ; t - texto


cadena = "\nEsta es una linea añadida al fichero" #añadimos el salto de linea para que no escriba justo a continuación

fichero.write(cadena)

fichero.close()
