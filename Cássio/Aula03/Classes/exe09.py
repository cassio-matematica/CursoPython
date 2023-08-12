class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def imprimir_informacoes(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Ano:", self.ano)
# Teste do exercício
livro = Livro("Aprendendo Python", "João Silva", 2021)
livro.imprimir_informacoes()  # Saída: Título: Aprendendo Python, Autor: João Silva, Ano: 2021
