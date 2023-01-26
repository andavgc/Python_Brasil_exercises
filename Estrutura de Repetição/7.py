#Faça um programa que leia 5 números e informe o maior número.

numeros = []

for num in range(5):
    num = int(input("inserte um número: "))
    numeros.append(num)

ordem = sorted(numeros)

print(f"O maior número é {ordem[-1]}")