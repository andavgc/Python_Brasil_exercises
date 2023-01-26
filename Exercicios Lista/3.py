#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = [2, 4, 5, 9]
soma = 0
for n in notas:
    soma += n
    print(n)

media = soma / len(notas)
print(f"média: {media}")