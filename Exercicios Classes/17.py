from bichinho import BichinhoVirtual
vivos = True
vaca = BichinhoVirtual("Vaca")
frango = BichinhoVirtual("Frango")
porco = BichinhoVirtual("Porco")
bichinho_1 = vaca

while vivos:
    lista = [vaca, frango, porco]
    atributos = f"nome: {bichinho_1.nome}\nidade: {bichinho_1.idade}\nfome: {bichinho_1.fome}\nsaude: {bichinho_1.saude}\ntedio: {bichinho_1.tedio}\nhumor: {bichinho_1.humor}\n"
    for animal in lista:
        animal.alterarFome()
        animal.fome += 1
        animal.tedio += 1
        bichinho_1 = animal
        atributos = f"nome: {bichinho_1.nome}\nidade: {bichinho_1.idade}\nfome: {bichinho_1.fome}\nsaude: {bichinho_1.saude}\ntedio: {bichinho_1.tedio}\nhumor: {bichinho_1.humor}\n"
        print(atributos)
    menu_1  = "1. vaca\n2. frango\n3. porco\n4. todos"
    menu_2 = "1. Alterar nome\n2. Dar de comer\n3. Brincar\n4. Nada"

    print(menu_1)
    bichinho = 0
    while bichinho not in [1,2,3,4]:
        bichinho = int(input("Com qual bichinho quer interagir?\n"))

    if bichinho == 1:
        bichinho_1 = vaca
    elif bichinho == 2:
        bichinho_1 = frango
    elif bichinho == 3:
        bichinho_1 = porco
    elif bichinho == 4:
        pass


    print(menu_2)
    acao = int(input("O que deseja fazer com o bichinho?\n"))

    if bichinho == 4:
        if acao == 1:
            for animal in lista:
                novo_nome = input(f"Digite o novo nome pra {animal.nome}: ")
                animal.alterarNome(novo_nome)
                print(f"novo nome do {animal.nome} alterado para: {animal.nome}")
        elif acao == 2:
            comida = int(input("Digite a quantidade que quer dar pra seus bichinhos: "))
            for animal in lista:
                animal.comer(comida)
                print(f"fome do {animal.nome}: {animal.fome}")
        elif acao == 3:
            tempo = int(input("Digite o novo nome pra seus bichinhos: "))
            for animal in lista:
                animal.brincar(tempo)
                print(f"tedio do {animal.nome}: {animal.tedio}")
        elif acao == 4:
            pass
        elif acao == 6:
            pass
    else:
        if acao == 1:
            novo_nome = input("Digite o novo nome pro seu bichinho: ")
            bichinho_1.alterarNome(novo_nome)
        elif acao == 2:
            comida = int(input("digite a quantidade que quer dar: "))
            bichinho_1.comer(comida)
        elif acao == 3:
            tempo = int(input("Digite quanto tempo quer brincar: "))
            bichinho_1.brincar(tempo)
        elif acao == 4:
            pass
        elif acao == 6:
            pass


