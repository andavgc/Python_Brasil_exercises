#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário.
#Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

salario = int(input("indique o salario inicial: "))
ano_inicial = 1995
ano_final = 2022
anos_trabalho = ano_final - ano_inicial
aumento = 0.015

for ano in range(anos_trabalho):
    if ano == 0:
        print(f"{ano_inicial}: {salario:.2f}")
        continue
    else:
        ano_inicial += 1
        aumento *= 2
        salario += (salario*aumento)
        print(f"{ano_inicial}: {salario:.2f} (aumento: {aumento * 100}%)")