#Faça um programa que calcule o mostre a média aritmética de N notas.

import statistics
notas = []
num = 1
teste = int(input("quantas provas são? "))
nota = 0

for nota in range(teste):
    nota = int(input(f"insira a nota da prova nº{num}: "))
    notas.append(nota)
    num += 1

media = statistics.mean(notas)

print(f"media das notas: {media}")