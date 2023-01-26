#Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
#Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente():
    def __init__(self, numero_conta, nome_correntista):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = 0

    def alterarNome(self):
        self.nome_correntista = input("Digite o novo nome: ")
        return self.nome_correntista

    def deposito(self):
        deposito = float(input("Digite o valor que deseja depositar: "))
        self.saldo += deposito
        return self.saldo

    def saque(self):
        saque = float(input("Digite o valor que deseja sacar: "))
        self.saldo -= saque
        return self.saldo

conta_1 = ContaCorrente(123456, "Andrés", 19000)

conta_1.saldo = 19000

print(conta_1.saldo)