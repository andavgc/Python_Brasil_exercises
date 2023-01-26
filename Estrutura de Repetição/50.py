#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

s = int(input("quantas series?: "))
m = 1
resultado = 0

print("H =", end=" ")
for n in range(s):
    if n+1 == s:
        print(f"1/{m}")
    else:
        print(f"1/{m}", end=" + ")
    div = 1/m
    resultado += div
    m += 1

print(f"n = {resultado}")
