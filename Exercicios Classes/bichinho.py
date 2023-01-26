class BichinhoVirtual():
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 10
        self.idade = 0
        self.tedio = 0
        self.humor = ((self.saude * 10) - (self.fome * 10)) / 10

    def alterarNome(self, nome):
        self.nome = nome
        return self.nome

    def alterarFome(self):
        self.fome += 1

    def comer(self, qtd):
        if qtd > self.fome:
            self.fome = 0
        else:
            self.fome -= qtd

    def brincar(self, tmp):
        self.tedio -= (tmp/10)
        if self.tedio > 0:
            self.tedio = 0

    def doenca(self, grau):
        self.saude -= grau

    def Aniversario(self):
        self.idade += 1