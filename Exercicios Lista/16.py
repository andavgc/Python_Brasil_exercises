#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
#O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
#Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
#Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#$200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 em diante

#Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

vendas = []
continuar = True
inicio = 200
final = 300

while continuar:
    venda = int(input("Insira o valor da suas vendas: "))
    comissao = venda * 0.09
    salario = 200 + comissao
    vendas.append(salario)
    cont = input("deseja registrar mais vendas? (y/n): ")
    if "n" in cont:
        continuar = False
        break

asalariados = []

for z in range(9):
    a = 0
    for x in vendas:
        if inicio < 1000:
            if x in range(inicio, final):
                a += 1
        else:
            if x >= inicio:
                a += 1
    asalariados.append(a)
    inicio += 100
    final += 100


print("Vendedores que receberam:")
for (x,s) in zip(range(200, 1000, 100), asalariados):
    print(f"entre R${x} e R${x+99}: {s}")

print(f"R$1000 em diante: {asalariados[-1]}")