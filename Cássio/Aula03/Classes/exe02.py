class Cachorro:
    def __init__(cachorro, nome, idade, som):
        cachorro.nome = nome
        cachorro.idade = idade
        cachorro.som = som

    ####Criando um método para o cachorro
    def imprime_Dados(cachorro):
        print("O nome do cachorro é " , cachorro.nome)
        print("Sua idade é  ", cachorro.idade)
    def late (cachorro):
        print("O rex sabe latir", cachorro.som)


##Criando um novo objeto cachorro


rex = Cachorro("Rex", 8, "au, au")

rex.imprime_Dados()
rex.late()
        
