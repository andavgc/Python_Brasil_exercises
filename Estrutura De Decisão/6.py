#Faça um Programa que leia três números e mostre o maior deles.

lista = []

for a in range(3):
    a = int(input("ingresse um número: "))
    lista.append(a)

lista.sort()
print(lista[-1])