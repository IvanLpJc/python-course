class Coche:
    def __init__(self, marca, color, combustible, cilindrada) -> None:
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrar_caracteristicas(self):
        print(f"El coche es un {self.marca}, de color {self.color}, utiliza {self.combustible} y tiene un motor de {self.cilindrada} litros")


media = lambda n1,n2,n3: (n1+n2+n3)/3