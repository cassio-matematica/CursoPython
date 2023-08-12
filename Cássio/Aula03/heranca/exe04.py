import math

class Forma:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

# Teste do exercício
retangulo = Retangulo(4, 3)
print("Área do retângulo:", retangulo.calcular_area())  # Saída: Área do retângulo: 12
print("Perímetro do retângulo:", retangulo.calcular_perimetro())  # Saída: Perímetro do retângulo: 14

circulo = Circulo(5)
print("Área do círculo:", circulo.calcular_area())  # Saída: Área do círculo: 78.53981633974483
print("Circunferência do círculo:", circulo.calcular_perimetro())  # Saída: Circunferência do círculo: 31.41592653589793
