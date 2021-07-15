print("*********************************************")
print("          Base de datos: Crear bd            ")
print("*********************************************")

import sqlite3
import os
# Con connect conectamos con una base de datos existente 
# o creamos una nueva si no existe y devuelve el enlace 
# a la bd

here = os.path.dirname(__file__)
bdname = "basededatos1.db"
bdpath = os.path.join(here, bdname)


conexion = sqlite3.connect(bdpath)
if(conexion):
    print("Base de datos creada")
conexion.close() # Si no la cerramos puede haber problemas


# Vamos a utilizar DB Browser for Sqlite para consultar los 
# archivos de base de datos

