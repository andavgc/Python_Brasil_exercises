class BombaCombustivel():
    def __init__(self, tipo, valor, qtd):
        self.tipoCombustivel = tipo
        self.valorLitro = valor
        self.quantidadeCombustivel = qtd

    def abastecerPorValor(self, valor):
        litros = valor / self.valorLitro
        return litros

    def abastecerPorLitro(self, litros):
        valor = litros * self.valorLitro
        self.quantidadeCombustivel += litros
        return valor

    def alterarValor(self, valor):
        self.valorLitro = valor
        return self.valorLitro

    def alterarCombustivel(self, tipo):
        self.tipoCombustivel = tipo
        return self.tipoCombustivel

    def alterarQuantidadeCombustivel(self, qtd):
        self.quantidadeCombustivel = qtd
        return self.quantidadeCombustivel

