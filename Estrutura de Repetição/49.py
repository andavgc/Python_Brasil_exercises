#Faça um programa que mostre os n termos da Série a seguir:
#  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
#Imprima no final a soma da série.

s = int(input("quantas series?: "))
m = 1
resultado = 0

print("S =", end=" ")
for n in range(s):
    if n+1 == s:
        print(f"{n+1}/{m}")
    else:
        print(f"{n+1}/{m}", end=" + ")
    div = n/m
    resultado += div
    m += 2

print(resultado)
