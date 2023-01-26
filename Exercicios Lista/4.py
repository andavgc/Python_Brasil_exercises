#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

p = "importante"
v = "aeiou"
q = 0

for c in p:
    if c not in v:
        q += 1
        print(c)
print(f"foram lidas {q} consoantes")