#Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
#Atributos: Nome, Fome, Saúde e Idade
#b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
#Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos
#Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
from datetime import date, time, datetime, timedelta
import time
import random
import threading
from joblib import Parallel, delayed

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

    def doenca(self, grau):
        self.saude -= grau
        self.saude -= 1

    def Aniversario(self):
        self.idade += 1

#criação do bichinho e dados pra salvar
print("Bichinho virtual")
nome = input("Digite o nome do seu bichinho: ")
bichinho_1 = BichinhoVirtual(nome)
dados_bichinho_inicio = open("bichinho_inicio.txt", "w")
dados_bichinho_inicio.write(f'{bichinho_1.nome}\n{bichinho_1.fome}\n{bichinho_1.saude}\n{bichinho_1.idade}\n{bichinho_1.tedio}\n{bichinho_1.humor}')
dados_bichinho_inicio.close()
print(f"{bichinho_1.nome}! que lindo nome, vamos a aprender a cuidar dele agora: ")
dados_bichinho = dados_bichinho_inicio

#preparacao pro menu de interacoes
menu = "1. Alterar nome\n2. Dar de comer\n3. Brincar\n4. Nada"
atributos = f"nome: {bichinho_1.nome}\nidade: {bichinho_1.idade}\nfome: {bichinho_1.fome}\nsaude: {bichinho_1.saude}\ntedio: {bichinho_1.tedio}\nhumor: {bichinho_1.humor}"
vivo = True
saudavel = True
dia = 1
ano = 1
data = time.localtime()




#interacoes com o bichinho
while vivo:
    #passo do tempo
    dia += 1
    print(f"ano {ano}")
    print(f"dia {dia}")
    time.sleep(1)

    if dia == 366:
        dia = 0
        ano += 1
        print(f"ano {ano}")
        print(f"dia {dia}")

    #modificacoes atraves do tempo

    #fome
    threading.Thread(target=bichinho_1.alterarFome).start()
    print(atributos)
    time.sleep(12)

    #doença
    # probabilidade
    n = random.randrange(0,100)
    print(n)
    time.sleep(15)

    if n in [1,2,3,4,5]:
        print(f"Oh não, {bichinho_1.nome} está doente! a saude dele está diminuindo constantemente")
        saudavel = False
        grau = random.randrange(1,5)
        tempo = random.randrange(240, 2000)
        bichinho_1.doenca(grau)
        print(atributos)
        recuperacao = 0

        if recuperacao > tempo:
            recuperacao += 1
            time.sleep(1)

        while saudavel == False:
            bichinho_1.doenca(1)
            print(atributos)
            time.sleep(240)

        if recuperacao == tempo:
            saudavel = True
            print(f"{bichinho_1.nome} melhorou depois de muito cuidado, a saude se recuperará com o tempo")

    #interacoes
    print(menu)
    acao = int(input("O que deseja fazer com o bichinho?"))

    if acao == 1:
        novo_nome = input("Digite o novo nome pro seu bichinho: ")
        bichinho_1.alterarNome(novo_nome)
    elif acao == 2:
        comida = int(input("digite a quantidade que quer dar: "))
        bichinho_1.comer(comida)
    elif acao == 3:
        tempo = int(input("Digite quanto tempo quer brincar: "))
        bichinho_1.brincar(tempo)
    elif acao == 4:
        pass


