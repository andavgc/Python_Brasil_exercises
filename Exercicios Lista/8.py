#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []

for n in range(5):
    idade = int(input("Insira sua idade: "))
    idades.append(idade)
    altura = float(input("Insira sua altura: "))
    alturas.append(altura)

for (i, a) in zip(reversed(idades), reversed(alturas)):
    print(f"idade: {i}, altura: {a}")