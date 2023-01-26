#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

import math

MB = int(input("digite o peso do arquivo a baixar (em MB): "))
velocidade = int(input("digite a velocidade de download (em mbps): "))

tamanho = MB * 8
tempo_segundos = (tamanho / velocidade)
minutos = tempo_segundos / 60
segundos = (minutos - math.floor(minutos)) * 60

input("O arquivo vai demorar %d minutos e %d segundos em baixar" % (minutos, segundos))
