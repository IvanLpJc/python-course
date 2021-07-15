def saludar(nombre):
    """
    Esto será un comentario de la funcion saludar.
    Esta recibirá como parámetro una cadena con el nombre
    e imprimirá un saludo con el nombre concatenado
    """
    print("Buenos días " + nombre)

saludar("Iván")

#help(saludar)
# Nos mostraría por pantalla:

# saludar(nombre)
#     Esto será un comentario de la funcion saludar.
#     Esta recibirá como parámetro una cadena con el nombre
#     e imprimirá un saludo con el nombre concatenado

class Saludos:
    """
    Esta clase tendrá dos funciones:
        - buenos_dias
        - adios
    Ambas funciones recibirán un nombre
    """

    def buenos_dias(self, nombre):
        """
        Esta funcion sirve para decir buenos días
        """
        print("Buenos días " + nombre)

    def adios(self, nombre):
        """
        Esta funcion sirve para despedirse
        """
        print("Adios " + nombre )

saludo = Saludos()

saludo.buenos_dias('Iván')
saludo.adios('Iván')

help(Saludos)

#También podemos utilizar la función help() para ver la documentación de otros métodos de python