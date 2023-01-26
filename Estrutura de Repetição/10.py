#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles

a = int(input("inserte o primeiro numero: "))
b = int(input("inserte o segundo numero: "))

for x in range((a + 1), b):
    print(x)