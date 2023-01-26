#Faça um Programa que peça dois números e imprima o maior deles.

a = int(input("primeiro numero: "))
b = int(input("segundo numero: "))

lista = [a, b]
lista.sort()

print(lista[-1])