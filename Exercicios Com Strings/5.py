nome = input('digite seu nome: ').upper()


for x in nome:
    print(nome)
    nome = nome.replace(nome[-1], "")
