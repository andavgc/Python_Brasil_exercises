#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
#mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00

valor_hora = int(input("digite quanto você ganha por hora (em R$): "))
horas = int(input("digite quantas horas você trabalha ao mês: "))

salario = valor_hora * horas

while salario <= 0:
    print("valores invalidos!")
    valor_hora = int(input("digite quanto você ganha por hora (em R$): "))
    horas = int(input("digite quantas horas você trabalha ao mês: "))
    salario = valor_hora * horas
    continue
else:
    if salario <= 900:
        IR = 0
        desc_ir = "0%"
    elif 900 < salario <= 1500:
        IR = salario * 0.05
        desc_ir = "5%"
    elif 1500 < salario <= 2500:
        IR = salario * 0.1
        desc_ir = "10%"
    else:
        IR = salario * 0.2
        desc_ir = "20%"
#print(salario, IR)
INSS = salario * 0.1
desc_inss = "10%"
FGTS = salario * 0.11
desc_fgts = "11%"
descontos = IR + INSS
salario_liquido = salario - descontos

print("Salário Bruto: (%d * %d)          : R$ %d\n" %(valor_hora, horas, salario),
      "(-) IR (%s)                     : R$ %d\n" %(desc_ir, IR),
      "(-) INSS (%s)                   : R$ %d\n" %(desc_inss, INSS),
      "FGTS (%s)                       : R$ %d\n" %(desc_fgts, FGTS),
      "Total de descontos               : R$ %d\n" %descontos,
      "Salário Liquido                  : R$ %d\n" %salario_liquido)