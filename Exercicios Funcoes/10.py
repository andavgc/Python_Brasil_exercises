#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12.
#Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
#Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
#Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
import random
import functions

print("Bem-vindo ao jogo de Craps.")
print('Lance dois dados, se na primeira vez você tirar 7 ou 11, você ganha! Mas se tirar 2,3 ou 12, você perde')
print('Se você tirar qualquer outro número, você terá que tirar esse número novamente, antes de tirar 7, caso contrário você perde!')

continuar = True
c = ''
while continuar:
    while c not in ['y', 'n']:
        c = input('Quer começar? (y/n): ').lower()

    if c == 'y':
        print('Jogando os dados...')
        dado_1 = random.randrange(1, 7)
        dado_2 = random.randrange(1, 7)
        print(f'dado n1: {dado_1}')
        print(f'dado n2: {dado_2}')
        valor = dado_1 + dado_2
        if valor in [7, 11]:
            print('Você ganhou! Parabéns')
        elif valor in [2, 3, 12]:
            print('Você perdeu :( tente novamente')
        else:
            n = ''
            valor_2 = str(valor)
            while valor_2 not in [7, valor]:
                n = input(f'Você tirou {valor_2}, jogar os dados novamente? (y/n): ')
                if n == 'y':
                    print('Jogando os dados...')
                    dado_1 = random.randrange(1, 7)
                    dado_2 = random.randrange(1, 7)
                    print(f'dado n1: {dado_1}')
                    print(f'dado n2: {dado_2}')
                    valor_2 = dado_1 + dado_2

                    if valor_2 == 7:
                        print('Você tirou 7, game over :(')
                    elif valor_2 == valor:
                        print(f'Você tirou {valor_2}! Parabéns você é um vencedor!!!')
                        cont = input('Jogar novamente? (y/n): ').lower()
                        if cont == 'y':
                            continue
                        else:
                            print('Jogo encerrado, obrigado por participar!')
                            continuar = False
                            break
                else:
                    print('Jogo encerrado, obrigado por participar!')
                    continuar = False
                    break
    elif c == 'n':
        print('Jogo encerrado, obrigado por participar!')
        continuar = False
        break