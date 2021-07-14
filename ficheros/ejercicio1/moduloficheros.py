import os

class Fichero:
    def fichero_existe(self, fichero):
        here = os.path.dirname(__file__)
        filepath = os.path.join(here, fichero)
        if(os.path.isfile(filepath)):
            return True
        
        return False

    def leer_fichero(self, fichero):

        here = os.path.dirname(__file__)
        filepath = os.path.join(here, fichero)
        if(os.path.isfile(filepath)):
            fichero = open(filepath, "rt")

            datos = fichero.read()
            
            fichero.close()
            return datos
        else:
            print("El fichero no existe")

    def grabar_fichero(self, fichero):
        here = os.path.dirname(__file__)
        filepath = os.path.join(here, fichero)
        fichero = open(filepath, "wt")
        if(os.path.isfile(filepath)): 
            print("Fichero creado con exito")
            fichero.close()
        else:
            print("Error creando el fichero")

    def incluir_fichero(self, fichero):
        here = os.path.dirname(__file__)
        filepath = os.path.join(here, fichero)
        fichero = open(filepath, "at")
        print("Escriba el contenido a introducir en el fichero, presione tecla enter sin texto para salir")
        datos = input()
        while(datos != ""):
            datos = "\n" + datos
            fichero.write(datos)
            print("Escriba el contenido a introducir en el fichero, presione tecla enter sin texto para salir")
            datos = input()
        
        fichero.close()

    def eliminar_fichero(self, fichero):
        try:
            here = os.path.dirname(__file__)
            filepath = os.path.join(here, fichero)
            os.remove(filepath)
        except FileNotFoundError:
            print("El fichero a eliminar no existe")
    
    def show_files_in_folder(self):
        here = os.path.dirname(__file__)
        with os.scandir(here) as files:
            print([file.name for file in files])