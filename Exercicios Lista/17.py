#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
#Atleta: Rodrigo Curvêllo

#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m

#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m

atletas = []
medias = []
saltos_at = {}
continuar = True

while continuar:
    saltos = []
    atleta = input("Informe o nome do atleta: ")
    if atleta == "":
        continuar = False
        break
    else:
        atletas.append(atleta)

        for s in range(5):
            salto = float(input(f"Informe o salto Nº{s+1}: "))
            saltos.append(salto)

        #media
        media = sum(saltos) / len(saltos)
        print(f"Atleta: {atleta}\n"
              f"Primeiro Salto: {saltos[0]}\n"
              f"Segundo Salto: {saltos[1]}\n"
              f"Terceiro Salto: {saltos[2]}\n"
              f"Quarto Salto: {saltos[3]}\n"
              f"Quinto Salto: {saltos[4]}")
        medias.append(media)
    salto_at = ' - '.join(map(str, saltos))
    saltos_at[atleta] = salto_at


print("Resultado final: ")
for (med, at, sal) in zip(medias, saltos_at.keys(), saltos_at.values()):
    print(f"Atleta: {at}\n"
          f"Saltos: {sal}\n"
          f"Média dos saltos: {med:.1f} m")