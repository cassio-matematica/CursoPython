
class Animal:
    def __init__(animal, nome):
        animal.nome = nome
    
    def imprimir_cachorro(animal):
        print("O nome do animal é:", animal.nome)
    
    
class Cachorro(Animal):
        def emitir_som(cachorro):
            print("Au au!")
        

# Teste do exercício
animal = Animal("Joao")

cachorro = Cachorro()
cachorro.emitir_som()  


