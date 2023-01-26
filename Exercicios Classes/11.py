class Carro():
    def __init__(self, litros):
        self.consumoCombustivel = litros
        self.quantidadeCombustivel = 0

    def andar(self, km):
        if self.quantidadeCombustivel > 0:
            consumo = km / self.consumoCombustivel
            self.quantidadeCombustivel -= consumo
        else:
            print("O carro está sem combustivel")

    def obterGasolina(self):
        return self.quantidadeCombustivel

    def adicionarGasolina(self, qtd):
        self.quantidadeCombustivel += qtd


carro = Carro(10)
carro.adicionarGasolina(50)
