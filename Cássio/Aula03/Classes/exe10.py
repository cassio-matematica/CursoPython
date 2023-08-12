class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def aumentar_salario(self, percentual):
        self.salario *= (1 + percentual/100)
    
    def imprimir_dados(self):
        print("Nome:", self.nome)
        print("Salário:", self.salario)

# Teste do exercício
funcionario = Funcionario("João", 3000)
funcionario.aumentar_salario(10)
funcionario.imprimir_dados()  # Saída: Nome: João, Salário: 3300.0
