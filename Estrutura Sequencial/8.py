#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

dinheiro = int(input("digite quanto você ganha por hora em R$: "))
horas = int(input("digite as horas que você trabalha por mês: "))

salario = dinheiro * horas

print("o seu salario desse mês será %d" % salario)