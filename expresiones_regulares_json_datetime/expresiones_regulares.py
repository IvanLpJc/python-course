print("*********************************************")
print("      Expresiones Regulares: Search          ")
print("*********************************************")

# Es una secuencia de caracteres que forman una busqueda por patrón
# sirven para verificar si una cadena de texto contiene el patrón
import re # modulo para las expresiones regulares


texto = "Hola, mi nombre es Iván"
# Busca el patron: "nombre" dentro de "texto" 
# devuelve un objeto de tipo Match
resultado = re.search("nombre", texto) 

if(resultado):
    print("Cadena encontrada")
else:
    print("Cadena NO encontrada")

# Busca en la cadena si alguna frase termina en Iván
resultado = re.search("Iván$", texto) 
if(resultado):
    print("Cadena encontrada")
else:
    print("Cadena NO encontrada")


# Busca en la cadena si alguna frase empieza en Hola
resultado = re.search("^Hola", texto) 
if(resultado):
    print("Cadena encontrada")
else:
    print("Cadena NO encontrada")


# Podemos buscar por partes, por ejemplo, que apareca mi y es
# Con "." indicamos que puede aparecer un caracter en medio
# Con "*" indicamos que pueden aparecer 0 o más veces esos 
# caracteres en medio
resultado = re.search("mi.*es", texto) 
if(resultado):
    print("Cadena encontrada")
else:
    print("Cadena NO encontrada")

print("*********************************************")
print("      Expresiones Regulares: findall         ")
print("*********************************************")

texto = """
El coche de Luis es rojo,
el coche de Antonio es blanco,
y el coche de María es rojo
"""

# Busca todas las ocurrencias que haya de la cadena que contenga coche+<cualquier caracter>+rojo
resultado = re.findall("coche.*rojo", texto) 
if(resultado):
    print("Cadena encontrada")
    print(resultado) # ['coche de Luis es rojo', 'coche de María es rojo']
else:
    print("Cadena NO encontrada")

print("*********************************************")
print("       Expresiones Regulares: split          ")
print("*********************************************")

# Divide una cadena a partir de un patron
texto = "La silla es blanca y vale 80"
# Va a usar el \s (espacio en blanco) para dividir el texto
print(re.split("\s", texto)) # ['La', 'silla', 'es', 'blanca', 'y', 'vale', '80']

print("*********************************************")
print("        Expresiones Regulares: sub           ")
print("*********************************************")

# Sustituye todas las ocurrencias de una cadena
print(texto)
print(re.sub("blanca", "roja", texto)) # Sustituye blanca por rojo