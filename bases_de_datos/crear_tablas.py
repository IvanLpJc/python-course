print("*********************************************")
print("         Base de datos: Crear tablas         ")
print("*********************************************")

#SQLite 3 - Crear tablas en la base de datos

import sqlite3
import os

here = os.path.dirname(__file__)
bdname = "basededatos1.db"
bdpath = os.path.join(here, bdname)


conexion = sqlite3.connect(bdpath)

# Crea un objeto para poder ejecutar sentencias sql
cursor = conexion.cursor() 

# Execute nos permite ejecutar las sentencias
sql = "CREATE TABLE PERSONAS (nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)"
cursor.execute(sql)

# Con commit le decimos a la bd que guarde estos 
# cambios y los mantenga
conexion.commit()

conexion.close()