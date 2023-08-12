class Carro:
    def __init__(carro, marca, modelo, ano):
        carro.marca = marca
        carro.modelo = modelo
        carro.ano = ano
    
    def imprimir_informacoes(carro):
        print("Marca:", carro.marca)
        print("Modelo:", carro.modelo)
        print("Ano:", carro.ano)

# Teste do exercício
carro = Carro("Honda", "Civic", 2015)
carro.imprimir_informacoes()  # Saída: Marca: Ford, Modelo: Fiesta, Ano: 2020


