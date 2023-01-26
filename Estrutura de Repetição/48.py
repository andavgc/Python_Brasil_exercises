#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
#Exemplo:
#  12376489
#  => 98467321

numero = input("insira um numero inteiro: ")
invertido = ""

for n in reversed(numero):
    invertido += str(n)

print(invertido)
