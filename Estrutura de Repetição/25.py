#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

import statistics
idades = []
num = 1
pessoas = int(input("quantas pessoas são? "))
idade = 0

for idade in range(pessoas):
    idade = int(input(f"insira a idade da pessoa nº{num}: "))
    idades.append(idade)
    num += 1

media = statistics.mean(idades)
if media <= 25:
    grupo = "jovem"
if media > 60:
    grupo = "idosa"
else:
    grupo = "adulta"
print(f"A média de idade é {media}, a turma é {grupo}")