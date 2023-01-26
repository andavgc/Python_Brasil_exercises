#Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double).
# Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def retornarNome(self):
        print(self.nome)

    def retornarSalario(self):
        print(self.salario)

    def aumentarSalario(self, porc):
        self.salario += (self.salario * (porc / 100))

pedro = Funcionario("Pedro", 3200.00)

pedro.retornarNome()
pedro.retornarSalario()
pedro.aumentarSalario(10)
pedro.retornarSalario()
