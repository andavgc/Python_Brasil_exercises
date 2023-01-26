#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.

lista = {}
produto = []
precos = []
num = 0

for preco in range(3):
    num = num + 1
    produto = input("ingresse o %dº produto: " % num)
#    items.append(item)
    preco = int(input("ingresse o preço do produto em R$: "))
#    precos.append(preco)
    lista[produto] = preco

print(lista)

lista_o = sorted(lista.items(), key=lambda item: item[1])

print(lista_o[0][1])
for a, b in lista_o:
    print(a, b)
    barato = a
    print("Você deve comprar %s"% barato)
    break