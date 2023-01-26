#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

numeros = []

for x in range(10):
    x = int(input("Insira um numero: "))
    numeros.append(x)

print("numeros pares: ")
for x in numeros:
    if x % 2 == 0:
        print(x, end=" ")

print("\nnumeros impares: ")
for y in numeros:
    if y % 2 != 0:
        print(y, end=" ")