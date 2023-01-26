#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

A = [1,2,3,4,5,6,7,8,9,10]
res = 0

for n in A:
    res += (n**2)

print(res)