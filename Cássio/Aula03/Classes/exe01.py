
class Cliente:
    def __init__(cliente, nome, idade, e_mail, endereco):
        cliente.nome = nome
        cliente.idade = idade
        cliente.e_mail = e_mail
        cliente.endereco = endereco
    
    def imprimir_dados(cliente):
        print("Nome:", cliente.nome)
        print("Idade:", cliente.idade)
        print("e-mail:", cliente.email)
        print("Endereço:", cliente.endereco)

# Teste do exercício
cliente01 = Cliente("Cassio", 38, 'cassio.matematica@gmail.com', "Alto da Mooca")
cliente01.imprimir_dados()  # Saída: Nome: João


