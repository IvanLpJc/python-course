print("*********************************************")
print("     Base de datos: Insertar varias filas    ")
print("*********************************************")

import sqlite3
import os

here = os.path.dirname(__file__)
bdname = "basededatos1.db"
bdpath = os.path.join(here, bdname)


conexion = sqlite3.connect(bdpath)

# Crea un objeto para poder ejecutar sentencias sql
cursor = conexion.cursor() 

lista_personas = [
    ('Iván', 'López', 'Justicia', 24),
    ('Pedro', 'García', 'Aguado', 34),
    ('Andres', 'Iniesta', 'Noseque', 40)
]

# Usando executemany ejecuta esta sentencia reemplazando 
# las interrogaciones por cada uno de los elementos 
# correspondientes en la tupla que hay en cada elemento 
# de la lista

sql = "INSERT INTO PERSONAS VALUES (?,?,?,?)"

cursor.executemany(sql, lista_personas)

conexion.commit()

conexion.close()