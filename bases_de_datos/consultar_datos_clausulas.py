print("*********************************************")
print("        Base de datos: clausulas             ")
print("*********************************************")


print("*********************************************")
print("             Clausulas: where                ")
print("*********************************************")

import sqlite3
import os

here = os.path.dirname(__file__)
bdname = "basededatos1.db"
bdpath = os.path.join(here, bdname)


conexion = sqlite3.connect(bdpath)

# Crea un objeto para poder ejecutar sentencias sql
cursor = conexion.cursor() 

sql = "SELECT * FROM PERSONAS WHERE edad > 30"

cursor.execute(sql)

# Con fetchall podemos recoger todos los 
# resultados de la consulta

personas = cursor.fetchall()

for persona in personas:
    print(persona)

# Imprime:
#  ('Iván', 'López', 'Justicia', 24)
#  ('Iván', 'López', 'Justicia', 24)
#  ('Pedro', 'García', 'Aguado', 34)
#  ('Andres', 'Iniesta', 'Noseque', 40)

print("*********************************************")
print("            Clausulas: order by              ")
print("*********************************************")

sql = "SELECT * FROM PERSONAS ORDER BY edad"
cursor.execute(sql)
personas = cursor.fetchall()

for persona in personas:
    print(persona)
# Imprime
#     ('Iván', 'López', 'Justicia', 24)
#     ('Iván', 'López', 'Justicia', 24)
#     ('Pedro', 'García', 'Aguado', 34)
#     ('Andres', 'Iniesta', 'Noseque', 40)
conexion.close()