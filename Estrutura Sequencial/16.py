#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
import math

tinta = 18
valor_tinta = 80
casa = int(input("informe o tamanho da sua casa em m²: "))

litros = casa / 3
latas = math.ceil(litros / 18)
valor_final = latas * 80

print("Você precisa comprar %d latas de tinta e o valor será de R$%d" % (latas, valor_final))