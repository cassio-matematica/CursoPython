class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

# Teste do exercício
aluno = Aluno("Maria", [8, 9, 7])
media = aluno.calcular_media()
print("Média do aluno:", media)  # Saída: Média do aluno: 8.0
