#O cardápio de uma lanchonete é o seguinte:
#Especificação   Código  Preço
#Cachorro Quente 100     R$ 1,20
#Bauru Simples   101     R$ 1,30
#Bauru com ovo   102     R$ 1,50
#Hambúrguer      103     R$ 1,20
#Cheeseburguer   104     R$ 1,30
#Refrigerante    105     R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
#Considere que o cliente deve informar quando o pedido deve ser encerrado.

compra = True
codigo = ""
codigos = ["100", "101", "102", "103", "104", "105"]
valores = {}

items = []
valor_items = []

#cardápio
cardapio = "Especificação   Código  Preço\nCachorro Quente 100     R$ 1,20\nBauru Simples   101     R$ 1,30\nBauru com ovo   102     R$ 1,50\nHambúrguer      103     R$ 1,20\nCheeseburguer   104     R$ 1,30\nRefrigerante    105     R$ 1,00"
print(cardapio)

#adicionar items de compra
while compra:
      print("Para encerrar a compra aperte 'e'")
      print("Para abrir o cardápio, aperte 'c'")
      codigo = input("Insira o código do item:").lower()
      if codigo not in codigos:
            #encerrar venda
            if codigo == "e":
                  compra = False
                  break
            #abrir cardapio
            elif codigo == "c":
                  print(cardapio)
            continue
      else:
            #inserir quantidade do item desejado
            qtd = ""
            while type(qtd) is not float:
                  try:
                        qtd = float(input("Informe a quantidade: "))
                        continue
                  except:
                        continue
            #concatenar item comprado e quantidade à sacola
            #compras[codigo] += qtd

            if codigo == "100":
                  item = "Cachorro Quente"
                  valor = 1.2 * qtd
            elif codigo == "101":
                  item = "Bauru Simples"
                  valor = 1.3 * qtd
            elif codigo == "102":
                  item = "Bauru com ovo"
                  valor = 1.5 * qtd
            elif codigo == "103":
                  item = "Hambúrguer"
                  valor = 1.2 * qtd
            elif codigo == "104":
                  item = "Cheeseburguer"
                  valor = 1.3 * qtd
            elif codigo == "105":
                  item = "Refrigerante"
                  valor = 1 * qtd

            items.append(item)
            if codigo not in valores:
                  valores[codigo] = valor
            else:
                  valores[codigo] += valor
            valor_items.append(valor)


#print factura
for (i, v) in zip(items, valores.values()):
      print(f"{i}............R${v:.2f}")

valor_final = sum(valores.values())
print(f"total..................R${valor_final:.2f}")