class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangulo():
    def __init__(self, ponto, largura, altura):
        self.largura = largura
        self.altura = altura
        self.vertice = (ponto.x, ponto.y)

def valoresPonto(ponto):
    return f"({ponto.x}, {ponto.y})"

def centroRectangulo(Rectangulo):
    centro_x = (Rectangulo.largura/2) + Rectangulo.vertice[0]
    centro_y = (Rectangulo.altura/2) + Rectangulo.vertice[1]
    return Ponto(centro_x, centro_y)

continuar = True
while continuar:
    print("Centro de um rectângulo!\nPara começar, por favor digite o vértice inicial")

    x = int(input("Digite o valor de X: "))
    y = int(input("Digite o valor de Y: "))

    vertice_inicial = Ponto(x,y)

    print("Agora precisamos as medidas do rectângulo")
    largura = int(input("Digite a largura do rectângulo: "))
    altura = int(input("Digite a altura do rectângulo: "))

    rectangulo = Rectangulo(vertice_inicial, largura, altura)
    centro = centroRectangulo(rectangulo)

    print(f"O centro do triângulo se encontra no vértice: {valoresPonto(centro)}")

    continuar = input("Quer continuar? (y/n): ")

    if continuar == "n":
        print("Obrigado por participar")
        break