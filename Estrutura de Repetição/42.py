#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
# A entrada de dados deverá terminar quando for lido um número negativo.

num = 1
ate_25 = 0
ate_50 = 0
ate_75 = 0
ate_100 = 0
while num >= 0:
    num = int(input("Número: "))
    if num in range(1,26):
        ate_25 += 1
    elif num in range(26, 51):
        ate_50 += 1
    elif num in range(51, 76):
        ate_75 += 1
    elif num in range(76, 101):
        ate_100 += 1

print(f"Números entre 1 e 25: {ate_25}\n"
      f"Números entre 26 e 50: {ate_50}\n"
      f"Números entre 51 e 75: {ate_75}\n"
      f"Números entre 76 e 100: {ate_100}")