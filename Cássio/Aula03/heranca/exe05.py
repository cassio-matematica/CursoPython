class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

# Teste do exercício
gerente = Gerente("João", 5000, "Vendas")
print("Nome:", gerente.nome)  # Saída: Nome: João
print("Salário:", gerente.salario)  # Saída: Salário: 5000
print("Setor:", gerente.setor) # Saída: Setor: vendas
