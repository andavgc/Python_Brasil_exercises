#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

dinheiro = int(input("digite quanto você ganha por hora em R$: "))
horas = int(input("digite as horas que você trabalha por mês: "))

salario_b = dinheiro * horas
IR = salario_b * 0.11
INSS = salario_b * 0.08
sindicato = salario_b * 0.05
salario_l = salario_b - (IR + INSS + sindicato)

print("o seu salario bruto é: R$%d \n"
      "Imposto de renda: R$%d \n"
      "INSS: R$%d \n"
      "Sindicato: R$%d \n"
      "o seu salario liquido é: R$%d \n" % (salario_b, IR, INSS, sindicato, salario_l))