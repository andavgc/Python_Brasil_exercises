#Faça um Programa que leia três números e mostre-os em ordem decrescente.

numeros = []
ordem = 0

for numero in range(3):
    ordem = ordem + 1
    numero = int(input("inserte o %dº numero: " % ordem))
    numeros.append(numero)

numeros.sort(reverse=True)

for x in numeros:
    print(x)