#Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class TV():
    def __init__(self):
        self.tamanho = '55"'
        self.volume = 15
        self.canal = 1

    def mudarVolume(self, mudar):
        if mudar == "+":
            if self.volume == 100:
                pass
            self.volume += 1
        elif mudar == '-':
            if self.volume == 0:
                pass
            self.volume -= 1
        else:
            try:
                mudar = int(mudar)
                if 100 < mudar < 1:
                    print("o volume precisa ser entre 0 e 100")
                else:
                    self.volume = mudar
            except:
                print("parâmetro incorreto, tente novamente")

        return self.volume

    def mudarCanal(self, mudar):
        if mudar == "+":
            if self.canal == 100:
                pass
            self.canal += 1
        elif mudar == '-':
            if self.canal == 1:
                pass
            self.canal -= 1
        else:
            try:
                mudar = int(mudar)
                if 100 < mudar < 1:
                    print("o canal precisa ser maior a 0 e menor a 100")
                else:
                    self.canal = mudar
            except:
                print("parâmetro incorreto, tente novamente")

        return self.canal

tv = TV()
print(tv.canal, tv.volume)

tv.mudarCanal(54)
tv.mudarVolume(34)
print(tv.canal, tv.volume)