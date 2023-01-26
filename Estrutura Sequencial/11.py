#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#1) o produto do dobro do primeiro com metade do segundo .
#2) a soma do triplo do primeiro com o terceiro.
#3) o terceiro elevado ao cubo.

num_1 = int(input("inserte o primeiro numero inteiro: "))
num_2 = int(input("inserte o segundo numero inteiro: "))
num_3 = int(input("inserte um numero real: "))

calc_1 = (num_1 * 2) + (num_2 / 2)
calc_2 = (num_1 * 3) + num_3
calc_3 = num_3 ** 3

print("Os resultados são os seguintes: "
      "\n%d"
      "\n%d"
      "\n%d" % (calc_1, calc_2, calc_3))