
print("*********************************************")
print("*                Ejercicio 1                *")
print("*********************************************")

# Crear el modulo modulo1.py
# Añadir la clase coche creada en otro ejercicio
# Añadir una función lambda "media" creada en un ejericio anterior

# Crear un programa "ejercicio1.py"
# Importar el modulo1
# Crear un objeto coche 
# Mostrar las características del coche
# Calcular la media de 3 notas y mostrar el resultado

import modulo1

coche = modulo1.Coche('Peugeot', 'negro', 'diesel', '2.0')
coche.mostrar_caracteristicas()

media = modulo1.media(7,8,2)
print(media)