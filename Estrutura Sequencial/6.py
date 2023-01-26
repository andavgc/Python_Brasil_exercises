#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

R = float(input("digite o raio do círculo em centimetros: "))
π = 3.14159

A1 = π * (R ** 2)
A = float('%.2f'%A1)

print("A área do círculo é %d cm²" %A)