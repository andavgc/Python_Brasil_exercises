#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

import functions

a = int(input("Insira o primeiro número para soma: "))
b = int(input("Insira o segundo número para soma: "))
c = int(input("Insira o terceiro número para soma: "))

soma = functions.somar(a, b, c)

print(f'O resultado é {soma}')