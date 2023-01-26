#Classe Pessoa: Crie uma classe que modele uma pessoa:
#Atributos: nome, idade, peso e altura
#Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        return self.idade

    def engordar(self):
        self.peso += 1
        return self.peso

    def emagrecer(self):
        self.peso -= 1
        return self.peso
    
    def crescer(self):
        if self.idade < 21:
            self.altura += 0.5
        else:
            pass
        return self.altura

andres = Pessoa("Andrés", 15, 50, 165)

print(andres.envelhecer())