#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

import statistics
#input of each bimester note
A = float(input("nota do primeiro bimestre: "))
B = float(input("nota do segundo bimestre: "))
C = float(input("nota do terceiro bimestre: "))
D = float(input("nota do quarto bimestre: "))

#calculating the mean and rounding
data = [A, B, C, D]
X = statistics.mean(data)
mean = '%.2f'%X

print(mean)