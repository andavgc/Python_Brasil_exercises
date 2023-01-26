#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool: até 20 litros, desconto de 3% por litro, acima de 20 litros, desconto de 5% por litro
#Gasolina: até 20 litros, desconto de 4% por litro acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
#o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

combustivel = ""

while ("g" or "a") not in combustivel:
    combustivel = input("Escolha o tipo de combustivel [(G)asolina, (A)lcool]: ").lower()

litro = float(input("Insira os litros que deseja carregar: "))

if "a" in combustivel:
#R$1.90 o litro
    if litro <= 20:
        valor = litro * 1.843
    if litro > 20:
        valor = litro * 1.805

elif "g" in combustivel:
#R$2.50 o litro
    if litro <= 20:
        valor = litro * 2.4
    if litro > 20:
        valor = litro * 2.35

print(f"Você deve pagar {valor}")
