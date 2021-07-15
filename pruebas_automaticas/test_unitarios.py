# Sirve para crear pruebas dentro del propio código

def multiplicar(numero1, numero2):
    return numero1*numero1

resultado = multiplicar(2,4)
print(resultado)

import unittest

class pruebas(unittest.TestCase):
    # Definimos una clase para las pruebas que recibe TestCase
    # Definimos métodos para las pruebas
    # En este caso comprobamos que el resultado del método multiplicar
    # es el esperado para unos valores dados
    def test(self):
        self.assertEqual(multiplicar(2,4), 4)

# Código para que ejecute el test
if __name__ == '__main__':
    unittest.main()