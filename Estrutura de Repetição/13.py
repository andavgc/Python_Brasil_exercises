#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("insira a base: "))
exp = int(input("insira o exponente: "))

num = base

for x in range(exp - 1):
    num *= base
print(num)