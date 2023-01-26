#Faça um programa que leia 5 números e informe a soma e a média dos números
import statistics
numeros = []
soma = 0

for num in range(5):
    num = int(input("inserte um número: "))
    numeros.append(num)
    soma += num

media = statistics.mean(numeros)

print(f"soma = {soma}", f"media = {media}", sep="\n")