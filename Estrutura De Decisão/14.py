#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
#e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E

import statistics
#input of each bimester note
A = float(input("nota do primeiro parcial: "))
B = float(input("nota do segundo parcial: "))

#calculating the mean and rounding
# data = [A, B]
# X = statistics.mean(data)
mean = (A+B)/2

if 0 < mean <= 4.0:
    conceito = "E"
elif 4.0 <= mean < 6.0:
    conceito = "D"
elif 6.0 <= mean < 7.5:
    conceito = "C"
elif 7.5 <= mean < 9.0:
    conceito = "B"
elif mean >= 9.0:
    conceito = "A"

if conceito =="A" or conceito =="B" or conceito =="C":
    status = "APROVADO"
elif conceito =="D" or conceito =="E":
    status = "REPROVADO"

print("As suas notas do semestre foram %d e %d, você teve uma média de %.2f, o que le atribui nota %s. %s" % (A, B, mean, conceito, status))