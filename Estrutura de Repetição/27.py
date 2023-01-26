#Faça um programa que calcule o número médio de alunos por turma.
#Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

alunos_total = 0
num = 1
turmas = int(input("Quantidade de turmas: "))


for alunos in range(turmas):
    alunos = 50
    while alunos > 40:
        alunos = int(input(f"Alunos da turma n{num}: "))
    else:
        alunos_total += alunos
    num += 1

media = alunos_total / turmas

print(f"O número médio de alunos por turma é: {media}")