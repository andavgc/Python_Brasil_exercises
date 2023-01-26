#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.


carne = input("Escolha o tipo de carne [(F)ile duplo, (A)lcatra, (P)icanha]: ").lower()

kg = float(input("Insira os kg que deseja comprar: "))

if "f" in carne:
    carne = "File Duplo"
    if kg <= 5:
        valor = kg * 5.8
    if kg > 5:
        valor = kg * 4.9
elif "a" in carne:
    carne = "Alcatra"
    if kg <= 5:
        valor = kg * 6.8
    if kg > 5:
        valor = kg * 5.9
else:
    carne = "Picanha"
    if kg <= 5:
        valor = kg * 7.8
    if kg > 5:
        valor = kg * 6.9

print(f"o valor a pagar é de R${valor:.2f}")

pag = input("forma de pagamento: \n"
            "1 - Débito\n"
            "2 - Crédito\n"
            "3 - Dinheiro\n"
            "4 - Pix\n"
            "5 - Cartão Tabajara\n")

if pag == "5":
    dc = valor * 0.05
else:
    dc = 0.0

valor_final = valor - dc

print("---------------CUPOM FISCAL---------------\n"
      f"Carne:                    {carne}\n"
      f"Quantidade:               {kg}kg\n"
      "                                 \n"
      f"Valor bruto:              R${valor:.2f}\n"
      f"descontos:                R${dc:.2f}\n"
      f"Valor liquido:            R${valor_final:.2f}")