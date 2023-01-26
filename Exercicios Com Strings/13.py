#Jogo da palavra embaralhada.
#Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas.
#O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
#O jogador terá seis tentativas para adivinhar a palavra.
#Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
import random

#pegar uima palavra aleatoria do txt
palavras = open('Lista-de-Palavras.txt', 'r')
palavras_validas = []

#limpamos a lista de palavras para pegar palavras com certas condições
for p in palavras.readlines():
    if (len(p) > 3) and ('-' not in p):
        p = p.replace("\n", "")
        palavras_validas.append(p)

n_aleatorio = random.randint(0, len(palavras_validas)+1)
palavra = list(palavras_validas[n_aleatorio])
alvo = ''.join(palavra)
random.shuffle(palavra)
palavra = ''.join(palavra)
palavras.close()

#jogo
jogo = True
oportunidades = 6
print(alvo, "\n", palavra)

while oportunidades > 0:
    print(f"Oportunidades: {oportunidades}")
    chute = input("Digite seu chute: ").upper()
    if chute == alvo:
        print("Você venceu!")
        break
    else:
        print("chute errado, tente novamente")
        oportunidades -= 1

print("Fim do jogo!")