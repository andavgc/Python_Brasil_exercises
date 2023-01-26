votos = {"Windows Server": 0, "Unix": 0, "Linux": 0, "Netware": 0, "Mac OS": 0, "Outro": 0}
continuar = True

print("Qual o melhor Sistema Operacional para uso em servidores?\n\nAs possíveis respostas são:\n1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro")

while continuar:
    os = 99999
    if os not in range(1, 7):
        os = int(input("Número do Sistema Operacional (0=fim): "))

    if os == 0:
        continuar = False
        break
    else:
        if os == 1:
            votos["Windows Server"] += 1
        elif os == 2:
            votos["Unix"] += 1
        elif os == 3:
            votos["Linux"] += 1
        elif os == 4:
            votos["Netware"] += 1
        elif os == 5:
            votos["Mac OS"] += 1
        elif os == 6:
            votos["Outro"] += 1

#porcentaje de votos
porcentajes = {}
votos_totales = sum(votos.values())

for (p, v) in zip(votos.keys(), votos.values()):
    porc = (v*100)/votos_totales
    porcentajes[p] = porc

print("Sistema Operacional\t\t\tvotos\t%")
print("-------------------\t\t\t-----\t-----")
for (a, b, c) in zip(votos.keys(), votos.values(), porcentajes.values()):
    print(f"{a:<12}\t\t\t{b:9}\t{c:4.1f}%")
print("-------------------\t\t\t-----")
print(f"Total\t\t\t\t\t{votos_totales:9d}")

#reorganizar a lista
votos_1 = {}
sorted_keys = sorted(votos, key=votos.get, reverse=True)
for w in sorted_keys:
    votos_1[w] = votos[w]

melhor = list(votos_1.keys())[0]
votos_melhor = list(votos_1.values())[0]
i_melhor = list(votos).index(melhor)
porc_melhor = list(porcentajes.values())[i_melhor]

print(f"\nO Sistema Operacional mais votado foi {melhor}, com {votos_melhor} votos, correspondendo a {porc_melhor:.2f}% do total de votos")