#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo

a = int(input("inserte um numero: "))

if a > 0:
    print("valor é positivo")
elif a < 0:
    print("valor é negativo")
else:
    print("valor é zero")
