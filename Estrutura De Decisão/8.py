#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.

produto = []
mais_barato = None
num = 0

for i in range(3):
    num = num + 1
    produto = input("ingresse o %dº produto: " % num)
    preco = int(input("ingresse o preço do produto em R$: "))
    if mais_barato is None or mais_barato[0] > preco:
        mais_barato = (preco, produto)

print("Você deve comprar %s"% mais_barato[1])