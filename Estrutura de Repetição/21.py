#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

primo = True

num = int(input("insira um numero: "))
numeros = [2, 3, 5, 7, 9]

for x in numeros:
    resto = num % x
    if resto == 0 and num != x:
        primo = False
        print("Não é um numero primo")
        break

if primo:
    print("É um número primo")


