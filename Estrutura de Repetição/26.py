#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

#votos
c1 = 0
c2 = 0
c3 = 0
eleitor = 1
eleitores = int(input("Quantidade de eleitores: "))

for voto in range(eleitores):
    voto = 0
    while voto not in [1, 2, 3]:
        voto = int(input(f"Eleitor n{eleitor}: Para quem é seu voto? (candidato '1', '2' ou '3'): "))
    if voto == 1:
        c1 += 1
    elif voto == 2:
        c2 += 1
    elif voto == 3:
        c3 += 1
    eleitor+= 1

print(f"O candidato n1 teve um total de {c1} votos\n",
      f"O candidato n2 teve um total de {c2} votos\n",
      f"O candidato n3 teve um total de {c3} votos")
