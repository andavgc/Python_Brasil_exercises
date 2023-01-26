#Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo.
#A própria palavra leet admite muitas variações, como l33t ou 1337.
#O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet,
#sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo.
#Pesquise sobre as principais formas de traduzir as letras.
#Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.
import string
import random
alfabeto = list(string.ascii_lowercase)
dic_leet = []

#abrir arquivo com o dicionario leet
leet = open("leet.txt", "r")

#limpeza e organização
for letra in leet.readlines():
    letra = letra.split(",")
    for l in letra:
        i = letra.index(l)
        if " " in l:
            l = l.replace(" ", "")
        if "\n" in l:
            l = l.replace("\n", "")
        letra[i] = l
    dic_leet.append(letra)
leet.close()

#Substituição do texto:

#input do texto
index_letras = []
texto = input("Digite uma frase para convertir ao alfabeto leet: ").lower()
texto = list(texto)

#convertir letras em index
for letra in texto:
    if letra == " ":
        index_letras.append(" ")
        pass
    for l in alfabeto:
        if letra == l:
            i = alfabeto.index(l)
            index_letras.append(i)

#substituição
letra_texto = 0
for i in index_letras:
    n = -1
    if i == " ":
        letra_texto += 1
        pass
    for leet in dic_leet:
        n += 1
        if n == i:
            aleatorio = random.randint(0, len(leet)-1)
            letra_leet = leet[aleatorio]
            texto[letra_texto] = letra_leet
            letra_texto += 1
            break

texto = "".join(texto)
print(texto)