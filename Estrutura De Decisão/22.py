#Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
#Dica: utilize o operador módulo (resto da divisão).

numero = int(input("ingresse um número: "))

if numero == 0:
    print("O número é 0")
elif numero % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")
