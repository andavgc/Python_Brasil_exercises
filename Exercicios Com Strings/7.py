#Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#quantos espaços em branco existem na frase.
#quantas vezes aparecem as vogais a, e, i, o, u.

frase = input("Insira uma frase: ").lower()
espaco = 0
a, e, i, o, u = 0, 0, 0, 0, 0

for x in frase:
    if x == ' ':
        espaco += 1
    if x == 'a':
        a += 1
    if x == 'e':
        e += 1
    if x == 'i':
        i += 1
    if x == 'o':
        o += 1
    if x == 'u':
        u += 1

print(f'espaços em branco: {espaco}\n'
      f'letra a: {a}\n'
      f'letra e: {e}\n'
      f'letra i: {i}\n'
      f'letra o: {o}\n'
      f'letra u: {u}\n')