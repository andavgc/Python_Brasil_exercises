#Faça um Programa para leitura de três notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

import statistics
#input of each bimester note
A = float(input("nota do primeiro parcial: "))
B = float(input("nota do segundo parcial: "))
C = float(input("nota do terceiro parcial: "))

#calculating the mean and rounding
# data = [A, B]
# X = statistics.mean(data)
mean = (A+B+C)/3

if mean == 10:
    print("Aprovado com Distinção")
elif mean >= 7.0:
    print(f"Aprovado! Sua média foi {mean:.2f}")
else:
    print(f"Reprovado! Sua média foi {mean:.2f}")