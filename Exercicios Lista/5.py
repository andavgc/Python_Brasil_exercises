#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = []
pares = []
inpares = []

for n in range(20):
    num = int(input(f"insira o {n+1}º número: "))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        inpares.append(num)

print("números: %s\npares: %s\nimpares: %s" % (numeros, inpares, pares))