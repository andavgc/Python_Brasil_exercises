#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

F = int(input("digite a temperatura em graus Fahrenheit: "))

C = 5 * ((F-32) / 9)

print("%d graus Fahrenheit equivalem a %d graus Celsius" % (F, C))
