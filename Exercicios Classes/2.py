#Classe Quadrado: Crie uma classe que modele um quadrado:
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado():
    def __init__(self):
        self.lado = "15 cm"

    def MudarLado(self):
        self.lado = "20 cm"

    def RetornarLado(self):
        return self.lado

    def CalcularArea(self):
        lado = int(self.lado[0:2])
        self.area = str(lado ** 2) + " cm"
        return self.area

quadrado = Quadrado()

lado = quadrado.RetornarLado()
print("lado: ", lado)
quadrado.CalcularArea()
print("área: ", quadrado.area)
quadrado.MudarLado()
lado = quadrado.RetornarLado()
print("lado: ", lado)
quadrado.CalcularArea()
print("área: ", quadrado.area)