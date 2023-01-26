#Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
#Os juros e a quantidade de parcelas seguem a tabela abaixo:
#Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#1       0
#3       10
#6       15
#9       20
#12      25
#Exemplo de saída do programa:
#Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
#R$ 1.000,00     0               1                       R$  1.000,00
#R$ 1.100,00     100             3                       R$    366,00
#R$ 1.150,00     150             6                       R$    191,67

divida = int(input("Valor da dívida: "))
juros = 5

#juros
print(f" Valor da Dívida:\t\tValor dos Juros:\t\tQuantidade de Parcelas:\t\tValor da Parcela:")

for x in range(1, 13):
    if x in [1, 3, 6, 9, 12]:
        parcela = x
        if x == 1:
            juros = 0
        else:
            juros += 5
        valor_juros = int(divida * (juros*0.01))
        valor_divida = int(divida + valor_juros)
        valor_parcela = valor_divida / parcela
        print(f"\t  {valor_divida:10.2f}\t\t\t\t\t{valor_juros:4d}\t\t\t\t\t\t\t{parcela:3d}\t\t\t\t{valor_parcela:9.2f}")