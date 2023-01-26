#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#Código da cidade;
#Número de veículos de passeio (em 1999);
#Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#Qual a média de veículos nas cinco cidades juntas;
#Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

cidades =[]
veiculos = []
acidentes = []
cidades2k = []

for x in range(5):
    cod_cidade = input("digite o código da cidade: ")
    veiculo = int(input("Número de veículos de passeio: "))
    acidente = int(input("Número de acidentes de trânsito com vítimas: "))
    cidades.append(cod_cidade)
    veiculos.append(veiculo)
    acidentes.append(acidente)

max_acidentes = max(acidentes)
i_max_acidentes = acidentes.index(max_acidentes)
cidade_max_acidentes = cidades[i_max_acidentes]

print(f"O maior indice de acidentes de tránsito é de {max_acidentes} na cidade: {cidade_max_acidentes}")

min_acidentes = min(acidentes)
i_min_acidentes = acidentes.index(min_acidentes)
cidade_min_acidentes = cidades[i_min_acidentes]

print(f"O menor indice de acidentes de tránsito é de {min_acidentes} na cidade: {cidade_min_acidentes}")

media_veiculos = sum(veiculos) / len(veiculos)

print(f"A média de veículos é de {media_veiculos}")

for x in veiculos:
    if x < 2000:
        i_cidades2k = veiculos.index(x)
        acidentes2k = acidentes[i_cidades2k]
        cidades2k.append(acidentes2k)

media_acidentes2k = sum(cidades2k) / len(cidades2k)

print(f"A média de acidentes de tránsito nas cidades com menos de 2000 veículos é de {media_acidentes2k}")