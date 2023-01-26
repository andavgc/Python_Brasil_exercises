#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
#O usuário deverá informar a quantidade de CDs e o valor para em cada um.

gasto = 0
num = 1
cd = int(input("Quantidade de CDs: "))


for preco in range(cd):
    preco = int(input(f"preço do CD {num} em R$: "))
    gasto += preco
    num += 1

media = gasto / cd

print(f"O valor investido é de R${gasto}, e o valor médio gasto em cada CD é R${media}")