print("*********************************************")
print("          Base de datos: Borrar datos        ")
print("*********************************************")


import sqlite3
import os

here = os.path.dirname(__file__)
bdname = "basededatos1.db"
bdpath = os.path.join(here, bdname)


conexion = sqlite3.connect(bdpath)

# Crea un objeto para poder ejecutar sentencias sql
cursor = conexion.cursor() 

sql = "DELETE FROM PERSONAS WHERE nombre = 'Pedro'"

cursor.execute(sql)

conexion.commit()

conexion.close()