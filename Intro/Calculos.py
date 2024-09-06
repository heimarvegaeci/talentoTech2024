class Calculos:
    def __init__(self, lado):
        self.lado = lado

    def calcular_superficie(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return self.lado * 4