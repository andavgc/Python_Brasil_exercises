#Classe Retangulo: Crie uma classe que modele um retangulo:

#Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
#Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Rectangulo():
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def MudarLados(self):
        self.comprimento = input("insira o novo valor do comprimento: ")
        self.largura = input("insira o novo valor da largura: ")

    def RetornarLados(self):
        return (self.comprimento, self.largura)

    def CalcularArea(self):
        self.area = self.comprimento * self.largura
        return self.area

    def CalcularPerimetro(self):
        self.perimetro = self.comprimento + self.largura + self.comprimento + self.largura
        return self.perimetro

#-------------------------------------------------------

print("Informe as medidas de um local em metros: ")
comprimento = int(input("comprimento: "))
largura = int(input("largura: "))

rectangulo = Rectangulo(comprimento, largura)

pisos = rectangulo.CalcularArea()
rodapes = rectangulo.CalcularPerimetro()

print(f'precisaria {pisos}m² de piso e {rodapes}m de rodapé')

