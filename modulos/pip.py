# pip nos sirve para instalar nuevos modulos de python
# Nos vamos a terminal y con:
#  -> pip --version   -> podemos ver la version
#  -> pip list        -> nos lista los modulos que tenemos instalados 

# Si queremos un modulo que no está instalado usamos
#  -> pip install <nombre del modulo>
# por ejemplo: pip install camelcase

import camelcase

camel = camelcase.CamelCase()

texto = "mi nombre es ivan"
print(camel.hump(texto)) # Mi Nombre Es Ivan


#Para desinstalar usamos: pip uninstall <modulo>