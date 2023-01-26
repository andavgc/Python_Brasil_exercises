#Classe Bola: Crie uma classe que modele uma bola:
#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor

class Bola():
    def __init__(self):
        self.cor = "azul"
        self. circunferencia = "15 cm"

    def trocaCor(self):
        self.cor = "vermelho"

    def mostraCor(self):
        print(self.cor)

bola = Bola()
bola.material = "plástico"

bola.mostraCor()
bola.trocaCor()
bola.mostraCor()