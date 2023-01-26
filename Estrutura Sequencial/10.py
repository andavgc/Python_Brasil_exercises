#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

C = int(input("digite a temperatura em graus Celsius: "))

F = 32 + (C * (9/5))

print("%d graus Celsius equivalem a %d graus Fahrenheit" % (C, F))