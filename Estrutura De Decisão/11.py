#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = int(input("digite o seu salario em R$: "))

while salario <= 0:
    print("salario invalido!")
    salario = int(input("digite o seu salario em R$: "))
    continue
else:
    if salario <= 280:
        aumento = salario * 0.2
        percentagem = "20%"
        salario_novo = salario * 1.2
    elif 280 < salario <= 700:
        aumento = salario * 0.15
        percentagem = "15%"
        salario_novo = salario * 1.15
    elif 700 < salario <= 1500:
        aumento = salario * 0.1
        percentagem = "10%"
        salario_novo = salario * 1.1
    elif salario > 1500:
        aumento = salario * 0.05
        percentagem = "05%"
        salario_novo = salario * 1.05

print("O seu salario antigo era de R$%d, aplicando um aumento do %s (i.e R$%d) seu novo salario é R$%d"
      % (salario, percentagem, aumento, salario_novo))


