#Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() e digerir().
#Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.
#Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco():
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)
        return self.bucho

    def verBucho(self):
        print(f"bucho do {self.nome}: {self.bucho}")

    def digerir(self, alimento=None):
        if alimento != None:
            self.bucho.remove(alimento)
        else:
            self.bucho.remove(self.bucho[0])
        return self.bucho

pinky = Macaco("Pinky")
louis = Macaco("Louis")

pinky.comer("banana")
louis.comer("maçã")
pinky.verBucho()
louis.verBucho()

pinky.comer("lampada")
louis.comer("rocha")
pinky.verBucho()
louis.verBucho()

pinky.comer("árvore")
louis.comer(pinky)
pinky.verBucho()
louis.verBucho()

pinky.digerir()
louis.digerir()

pinky.verBucho()
louis.verBucho()

