#Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido.
#Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random

resultados = []
contagem = {}

#rodar dado
for d in range(100):
    dado = random.randrange(1, 7)
    resultados.append(dado)

#contar resultados
for n in range(1,7):
    cont = 0
    for x in resultados:
        if n == x:
            cont += 1
        contagem[n] = cont
    print(f'O número {n} apareceu {cont} vezes')