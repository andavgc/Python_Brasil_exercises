#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

valor_mor = 0
valor_mac = 0

mor = float(input("Insira quantos kg de morango deseja: "))
mac = float(input("Insira quantos kg de maça deseja: "))

if mor != 0:
    if mor <= 5:
        valor_mor = mor * 2.5
    if mor > 5:
        valor_mor = mor * 2.20
if mac != 0:
    if mac <= 5:
        valor_mac = mac * 1.8
    if mac > 5:
        valor_mac = mac * 1.5

valor = valor_mor + valor_mac

#conferir se existe desconto de 10%
kg = mor + mac

if (kg > 8) or (valor > 25):
    dc = valor * 0.1
    valor -= dc

print(f"Você deve pagar R${valor}")
