#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
#cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

A = [1,3,5,7,9,11,13,15,17,19]
B = [2,4,6,8,10,12,14,16,18,20]
E = [21,22,23,24,25,26,27,28,29,30]
G = []

for (c,d,f) in zip(A,B,E):
    G.append(c)
    G.append(d)
    G.append(f)

print(G)