class ContaBancaria:
    def __init__(contaBancaria, titular, saldo=0):
        contaBancaria.titular = titular
        contaBancaria.saldo = saldo
    
    def depositar(contaBancaria, valor):
        contaBancaria.saldo += valor
    
    def sacar(contaBancaria, valor):
        if valor <= contaBancaria.saldo:
            contaBancaria.saldo -= valor
        else:
            print("Saldo insuficiente")
    
    def imprimir_saldo(contaBancaria):
        print("Saldo:", contaBancaria.saldo)


# Teste do exercício
conta = ContaBancaria("João")
conta.depositar(100)
conta.sacar(50)
conta.imprimir_saldo()  # Saída: Saldo: 50
