#Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros.
# Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta.
# Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.

class ContaInvestimento():
    def __init__(self, saldo, juros):
        self.saldo = saldo
        self.taxaJuros = juros

    def adicioneJuros(self):
        self.taxaJuros += 1

conta = ContaInvestimento(1000, 10)

for x in range(5):
    conta.adicioneJuros()
    conta.saldo += conta.saldo * (conta.taxaJuros / 100)
print(conta.saldo)