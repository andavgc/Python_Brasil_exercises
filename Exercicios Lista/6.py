#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

alunos = []
notas = []

for a in range(10):
    aluno = input("Insira seu nome: ")
    alunos.append(aluno)
    soma = 0
    for n in range(4):
        nota = int(input(f"insira a {n+1}º nota: "))
        soma += nota
    media = soma / 4
    notas.append(media)

aprovados = 0
for s in notas:
    if s >= 7:
        aprovados += 1

print(f"Foram {aprovados} alunos com média maior ou igual a 7")
