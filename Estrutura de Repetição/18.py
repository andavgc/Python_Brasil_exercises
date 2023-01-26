#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

numeros = []

for num in range(5):
    num = int(input("inserte um numero de 1 a 1000: "))
    numeros.append(num)

min = min(numeros)
max = max(numeros)
sum = sum(numeros)

print(f"menor numero: {min}, maior numero: {max}, soma dos numeros: {sum}")