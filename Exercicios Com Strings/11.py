#Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
#O jogador poderá errar 6 vezes antes de ser enforcado.
import random

#pegar uima palavra aleatoria do txt
palavras = open('Lista-de-Palavras.txt', 'r')
palavras_validas = []

#limpamos a lista de palavras para pegar palavras com certas condições
for p in palavras.readlines():
    if (len(p) > 3) and ('-' not in p):
        p = p.replace("\n", "")
        palavras_validas.append(p)

random = random.randint(0, len(palavras_validas)+1)
palavra = palavras_validas[random]
palavras.close()

#jogo
oportunidades = 6
chute = "_ " * len(palavra)

while oportunidades > 0:
    print(f"Oportunidades: {oportunidades}")
    print(f"{len(palavra)} letras:\n\n"
          f"{chute}")

    posicoes = []
    letra = input('Digite uma letra: ').upper()

    if letra in palavra:
        num = 0
        #definir posicoes da letra
        for l in palavra:
            if letra == l:
                posicoes.append(num)
            num += 1

        #substituir o espaço em branco pela letra

        chute = list(chute)
        for i in posicoes:
            espaco = -1
            num = -1
            for e in chute:
                num += 1
                if e != " ":
                    espaco += 1
                    if espaco == i:
                        chute[num] = letra
        chute = "".join(chute)
        print('Essa letra está na palavra!')
        if palavra == chute.replace(" ", ""):
            print(chute)
            print("\nParabéns, você venceu!!!")
            break
    else:
        oportunidades -= 1
        print('Essa letra não está na palavra :(')
        continue

if oportunidades == 0:
    print(f"Você foi enforcado, a palavra era {palavra} tente novamente :(")