class Veiculo:
    def __init__(self, velocidade):
        self.velocidade = velocidade
    
    def acelerar(self):
        self.velocidade += 10

class Carro(Veiculo):
    def __init__(self, velocidade, marca):
        super().__init__(velocidade)
        self.marca = marca
    
    def ligar(self):
        print("Carro ligado")

# Teste do exercício
carro = Carro(0, "Ford")
carro.acelerar()
print("Velocidade do carro:", carro.velocidade)  # Saída: Velocidade do carro: 10
carro.ligar()  # Saída: Carro ligado
