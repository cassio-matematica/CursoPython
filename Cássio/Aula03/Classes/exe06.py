class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

# Teste do exercício
retangulo = Retangulo(4, 3)
area = retangulo.calcular_area()
perimetro = retangulo.calcular_perimetro()
print("Área do retângulo:", area)  # Saída: Área do retângulo: 12
print("Perímetro do retângulo:", perimetro)  # Saída: Perímetro do retângulo: 14
