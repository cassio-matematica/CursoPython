
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2
# Teste do exercício
triangulo = Triangulo(5, 3)
area = triangulo.calcular_area()
print("Área do triângulo:", area)  # Saída: Área do triângulo: 7.5
