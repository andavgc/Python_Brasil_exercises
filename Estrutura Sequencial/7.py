#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

A = float(input("digite a altura do quadrado em cm: "))
L = float(input("digite a largura do quadrado em cm: "))

area = A * L
d_area = area * 2

print("o dobro da área do quadrado é %d" % d_area)
