print("*********************************************")
print("        Base de datos: Insertar filas        ")
print("*********************************************")


import sqlite3
import os

here = os.path.dirname(__file__)
bdname = "basededatos1.db"
bdpath = os.path.join(here, bdname)


conexion = sqlite3.connect(bdpath)

# Crea un objeto para poder ejecutar sentencias sql
cursor = conexion.cursor() 

sql = "INSERT INTO PERSONAS VALUES ('Iván', 'López', 'Justicia', 24)"
cursor.execute(sql)

conexion.commit()

conexion.close()