#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input("informe o ano: "))
b = ano % 4

if b is 0:
    print("É um ano bissexto!")
else:
    print("Não é um ano bissexto!")