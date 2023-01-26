#Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
#Atributos: Nome, Fome, Saúde e Idade
#b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
#Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos
#Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
import os
import random
import time
from bichinho import BichinhoVirtual

#criação do bichinho e dados pra salvar
print("Bichinho virtual")
diretorio = '/home/andav/Python_Exercises/Python_Brasil/Exercicios Classes/bichinho_1.txt'

#carregar dados salvos do bichinho
if os.path.exists(diretorio):
    continuar = int(input("Deseja continuar jogando com o seu bichinho ou começar de zero?\n"
                      "1. Continuar\n"
                      "2. Começar de zero\n"))

    if continuar == 1:
        dados_bichinho = open("bichinho_1.txt", "r")
        dados_bichinho_1 = dados_bichinho.readlines()
        nome = dados_bichinho_1[0][0:-1]
        bichinho_1 = BichinhoVirtual(nome)
        bichinho_1.fome = int(dados_bichinho_1[1])
        bichinho_1.saude = int(dados_bichinho_1[2])
        bichinho_1.idade = int(dados_bichinho_1[3])
        bichinho_1.tedio = int(dados_bichinho_1[4])
        bichinho_1.humor = float(dados_bichinho_1[5])
    elif continuar == 2:
        pass

#criar novo bichinho
else:
    nome = input("Digite o nome do seu bichinho: ")
    bichinho_1 = BichinhoVirtual(nome)
    dados_bichinho_inicio = open("bichinho_inicio.txt", "w")
    dados_bichinho_inicio.write(f'{bichinho_1.nome}\n{bichinho_1.fome}\n{bichinho_1.saude}\n{bichinho_1.idade}\n{bichinho_1.tedio}\n{bichinho_1.humor}')
    dados_bichinho_inicio.close()
    print(f"{bichinho_1.nome}! que lindo nome, vamos a aprender a cuidar dele agora: ")
    dados_bichinho = dados_bichinho_inicio

#preparacao pro menu de interacoes
menu = "1. Alterar nome\n2. Dar de comer\n3. Brincar\n4. Nada"
vivo = True
saudavel = True

#interacoes com o bichinho
while vivo:

    #interacoes
    print(menu)
    acao = int(input("O que deseja fazer com o bichinho?\n"))

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
    elif acao == 6:
        print(atributos)

    #fome
    bichinho_1.alterarFome()

    #tedio
    bichinho_1.tedio += 1


    #doença
    # probabilidade
    time.sleep(15)
    n = random.randrange(0,100)
    print(n)


    if n in [1,2,3,4,5]:
        print(f"Oh não, {bichinho_1.nome} está doente! a saude dele está diminuindo constantemente")
        saudavel = False
        grau = random.randrange(1,5)
        tempo = random.randrange(240, 2000)
        bichinho_1.doenca(grau)
        print(atributos)
        recuperacao = 0

        while saudavel == False:

            if recuperacao > tempo:
                recuperacao += 1
            bichinho_1.doenca(1)
            print(atributos)

            if recuperacao == tempo:
                saudavel = True
                print(f"{bichinho_1.nome} melhorou depois de muito cuidado, a saude se recuperará com o tempo")
                break


    atributos = f"nome: {bichinho_1.nome}\nidade: {bichinho_1.idade}\nfome: {bichinho_1.fome}\nsaude: {bichinho_1.saude}\ntedio: {bichinho_1.tedio}\nhumor: {bichinho_1.humor}\n"
    print(atributos)

    #Salvar dados
    dados_bichinho = open("bichinho_1.txt", "w")
    dados_bichinho.write(
        f'{bichinho_1.nome}\n{bichinho_1.fome}\n{bichinho_1.saude}\n{bichinho_1.idade}\n{bichinho_1.tedio}\n{bichinho_1.humor}')

    dados_bichinho.close()