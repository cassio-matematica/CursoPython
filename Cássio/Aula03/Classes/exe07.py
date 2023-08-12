import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * (self.raio ** 2)
    
    def calcular_circunferencia(self):
        return 2 * math.pi * self.raio

# Teste do exercício
circulo = Circulo(5)
area = circulo.calcular_area()
circunferencia = circulo.calcular_circunferencia()
print("Área do círculo:", area)  # Saída: Área do círculo: 78.53981633974483
print("Circunferência do círculo:", circunferencia)  # Saída: Circunferência do círculo: 31.41592653589793
