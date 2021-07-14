print("*********************************************")
print("       JSON: Convertir dict a json           ")
print("*********************************************")

# Es una forma de almacenar e intercambiar datos en formato texto
import json


producto1 = {"nombre":"silla", 'color':'blanco','precio':80}

print("producto1: " + str(type(producto1)))
resultado = json.dumps(producto1)
print(resultado + "-> Resultado: " + str(type(resultado)))

print("*********************************************")
print("       JSON: Convertir json a dict           ")
print("*********************************************")

diccionario = json.loads(resultado)

print(f"{diccionario} -> Diccionario: " + str(type(diccionario)))