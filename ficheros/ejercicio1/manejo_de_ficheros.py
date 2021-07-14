# Esto es personal, he decidido hacerlo de forma ajena al curso

import os
from moduloficheros import Fichero
from subprocess import call

finish = ""
while(finish != "n"):
    print("Que desea hacer:")
    print("- Crear un fichero (c)")
    print("- Incluir texto en un fichero existente (i)")
    print("- Leer un fichero existente (l)")
    print("- Borrar un fichero (b)")
    print("- Mostrar archivos del directorio (m)")
    print("- Salir (s)")
    action = input()
    file = Fichero()

    if(action == 'c'):
        print("Introduce el nombre del fichero a crear:")
        filename = input()
        filename = filename +".txt" if ".txt" not in filename else ""
        if(not file.fichero_existe(filename)):
            file.grabar_fichero(filename)
        else:  
            print("El fichero ya existe")
    elif(action == 'i'):
        print("Introduce el nombre del fichero:")
        filename = input()
        filename = filename +".txt" if ".txt" not in filename else ""
        if(file.fichero_existe(filename)):
            file.incluir_fichero(filename)
        else:
            print("El fichero no existe")
    elif(action == 'l'):
        print("Introduce el nombre del fichero:")
        filename = input()
        filename = filename +".txt" if ".txt" not in filename else ""
        print(file.leer_fichero(filename))
    elif(action == 'b'):
        print("Introduce el nombre del fichero:")
        filename = input()
        filename = filename +".txt" if ".txt" not in filename else ""
        file.eliminar_fichero(filename)
    elif(action == 'm'):
        #file.show_files_in_folder()
        print("Ficheros en este directorio: \n")
        call('ls')
        print("\n")
    elif(action == 's'):
        finish = 'n'
    else:
        print("Acción inválida")
        print("Desea hacer algo más (y/n)")
        finish = input()
    
call('clear') # Ejecuta el comando clear en el terminal