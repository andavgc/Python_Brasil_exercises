#Faça um Programa que leia três números e mostre o maior e o menor deles.

lista = []
num = 0
for a in range(3):
    num = num + 1
    a = int(input("ingresse o %dº número: " % num))
    lista.append(a)

print("o maior número é %d e o menor é %d" % (max(lista), min(lista)))