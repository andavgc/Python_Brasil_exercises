#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.
# Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

n_aluno = []
alturas = []

for x in range(10):
    aluno = input("Informe o número de aluno: ")
    n_aluno.append(aluno)
    altura = int(input("informe sua altura em cm: "))
    alturas.append(altura)

#dados do mais alto
altura_alto = max(alturas)
index_alto = alturas.index(altura_alto)
n_alto = n_aluno[index_alto]

print(f"O usuario mais alto é {n_alto}\n",
      f"Altura: {altura_alto} cm", end='\n\n')

#dados do mais baixo
altura_baixo = min(alturas)
index_baixo = alturas.index(altura_baixo)
n_baixo = n_aluno[index_baixo]

print(f"O usuario mais alto é {n_baixo}\n",
      f"Altura: {altura_baixo} cm", end='\n\n')

