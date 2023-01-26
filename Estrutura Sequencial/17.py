#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor.
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

latas_t = 18
galoes_t = 3.6
valor_lata = 80
valor_galao = 25

casa = int(input("informe o tamanho da sua casa em m²: "))
#Quantidade de litros que precisa
litros = casa / 6
#print(litros)
#Quantidade de latas de tinta que precisa
latas = litros / latas_t
#print(latas)
#Quantidade de latas de tinta completas que precisa
latas_int = math.floor(latas)
#print(latas_sobrando)
#Quantidade de litros que sobram
litros_sobra = (latas - latas_int) * 18
#print(litros_sobra)
#Quantidade de galoes que precisa
galoes = math.ceil(litros_sobra / galoes_t)
#print(galoes)

if (latas - latas_int) <= 0.75:

so galao
so lata
galao e lata:
    #latas * 1,2,3 galao


if litros <= 3.6:
    print("Você precisa comprar 1 galão de tinta e o valor será de R$25")
else:
    if latas is int:
        valor_final = latas * 80
        print("Você precisa comprar %d latas de tinta e o valor será de R$%d" % (latas, valor_final))
    else:
        valor_final = (latas * valor_lata) + (galoes * valor_galao)
        print("Você precisa comprar %d latas e %d galoes de tinta e o valor será de R$%d" % (latas, galoes, valor_final))
