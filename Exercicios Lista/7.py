#aça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

v = [1, 2, 3, 4, 5]
s = 0
m = 1
for n in v:
    s += n
    m *= n

print(f"soma: {s}\nmultiplicação: {m}")