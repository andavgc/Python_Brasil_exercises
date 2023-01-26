#Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos.
#Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
#Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
pontuacoes = [' ', '!', '?', ',', ';', '.', ':', '(', ')']

frase = input(f'insira a frase o palavra: ').lower()

for y in pontuacoes:
    frase = frase.replace(y, '')

frase_inv = ''
for x in reversed(frase):
    frase_inv += x

if frase == frase_inv:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')