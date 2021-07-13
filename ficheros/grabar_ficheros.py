# Grabar un fichero de texto

# Creamos un fichero con open en modo write y texto
# Está utilizando la raiz del espacio de trabajo (carpeta python) 
# por eso especifico que debe ser dentro de la carpeta ficheros
fichero = open("./ficheros/fichero_para_grabar.txt","wt")
cadena_texto = "Hola, esta es la línea que vamos a grabar en el fichero de texto"

fichero.write(cadena_texto)

fichero.close()