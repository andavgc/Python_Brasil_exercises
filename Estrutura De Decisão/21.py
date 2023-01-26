#Faça um Programa para um caixa eletrônico.
#O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = 0
notas = []

while 10 > saque or saque > 600:
    saque = int(input("Qual é o valor do Saque? (min R$10, max R$600): "))

total = saque

for i in range(3):
    n = saque % 10
    notas.append(n)
    saque //= 10

u = notas[0]
d = notas[1]
c = notas[2]

notas_final = []

#definir centenas
if c > 0:
    if c > 1:
        nota_100 = f"{c} notas de R$100"
        notas_final.append(nota_100)
    elif c == 1:
        nota_100 = "1 nota de R$100"
        notas_final.append(nota_100)

#definir notas das decenas
if d >= 5:
    nota_50 = "uma nota de R$50"
    notas_final.append(nota_50)
    d -= 5
if d > 0:
    if d > 1:
        nota_10 = f"{d} notas de R$10"
        notas_final.append(nota_10)
    elif d == 1:
        nota_10 = "1 nota de R$10"
        notas_final.append(nota_10)
else:
    pass

#definir notas das unidades
if u >= 5:
    nota_5 = "uma nota de R$5"
    notas_final.append(nota_5)
    u -= 5
if u > 0:
    if u > 1:
        nota_1 = f"{u} notas de R$1"
        notas_final.append(nota_1)
    elif u == 1:
        nota_1 = "1 nota de R$1"
        notas_final.append(nota_1)
else:
    pass

#", ".join(notas_final[:-1]) + " e " + notas_final[-1]

print("Para o valor solicitado de R${} serão fornecidas: {}".format(total, ", ".join(notas_final[:-1]) + " e " + notas_final[-1] if len(notas_final) > 1 else "".join(notas_final)))
