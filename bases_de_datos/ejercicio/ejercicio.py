print("*********************************************")
print("          Base de datos: Ejercicio           ")
print("*********************************************")

print("""
Crear una base de datos 'basededatos.db
Crear una tabla 'productos' con 3 campos
 - id: Identificador de tipo numerico
 - nombre: tipo texto
 - precio: tipo numerico

Insertar 3 productos
 - 1,'Impresora',300
 - 2,'Ratón', 20
 - 3,'Ordenaror', 600

Consultar los productos de la tabla
Cerrar la bd
""")

import sqlite3
import os

here = os.path.dirname(__file__)
bdname = "basededatos.db"
bdpath = os.path.join(here, bdname)


conexion = sqlite3.connect(bdpath)

# Crea un objeto para poder ejecutar sentencias sql
cursor = conexion.cursor() 

# El campo id es auto incrementable cuanto creamos la tabla con (id INTEGER PRIMARY KEY...
# No es necesario utilizar el AUTO_INCREMENT
sql = "CREATE TABLE PRODUCTOS (id INTEGER PRIMARY KEY, nombre TEXT, precio NUMERIC)"

productos = [
    ('Impresora', 300),
    ('Ratón', 20),
    ('Ordenador', 600)
]

cursor.execute(sql)

conexion.commit()

sql = "INSERT INTO PRODUCTOS (nombre, precio) VALUES (?,?)"

cursor.executemany(sql, productos)

conexion.commit()

sql = "SELECT * FROM PRODUCTOS"

cursor.execute(sql)
# Con cursor.lastrowid podemos consultar cual ha sido el 
# último id añadido
#print("Last inserted: " + str(cursor.lastrowid))

productos = cursor.fetchall()

for producto in productos:
    print(producto)

conexion.close()