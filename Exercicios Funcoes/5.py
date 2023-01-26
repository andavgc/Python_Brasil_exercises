#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
#taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem,
#e custo, que é o custo de um item antes do imposto.
#A função “altera” o valor de custo para incluir o imposto sobre vendas.
import functions

custo = int(input("Valor do item: "))
imposto = input("Taxa de imposto: ")

valor_final = functions.SomaImposto(imposto, custo)

print(f'O valor com impostos é R${valor_final}')