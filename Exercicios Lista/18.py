votos = {}
continuar = True

print("Enquete: Quem foi o melhor jogador?")

while continuar:
    jug = 99999
    if jug not in range(1, 24):
        jug = int(input("Número do jogador (0=fim): "))

    if jug == 0:
        continuar = False
        break
    else:
        jug = str(jug)
        if jug not in votos:
            votos[jug] = 1
        else:
            votos[jug] += 1

    print(votos)

#reorganizar a lista
votos_1 = {}
sorted_keys = sorted(votos, key=votos.get, reverse=True)
for w in sorted_keys:
    votos_1[w] = votos[w]

#porcentaje de votos
porcentajes = {}
votos_totales = sum(votos_1.values())

for (p, v) in zip(votos_1.keys(), votos_1.values()):
    porc = (v*100)/votos_totales
    porcentajes[p] = porc

print(f"\nforam {votos_totales} votos computados.\n")

print("Jogador      votos         %")
for (a, b, c) in zip(votos_1.keys(), votos_1.values(), porcentajes.values()):
    print(f"      {a}          {b}     {c:.1f}%")

melhor = list(votos_1.keys())[0]
votos_melhor = list(votos_1.values())[0]
porc_melhor = list(porcentajes.values())[0]

print(f"\nO melhor jogador foi o número {melhor}, com {votos_melhor} votos, correspondendo a {porc_melhor}% do total de votos")