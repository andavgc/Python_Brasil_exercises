#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


turno = input("digite o seu turno (M-matutino ou V-Vespertino ou N- Noturno): ").lower()
valido = ["m", "v", "n"]

while turno not in valido:
    print("Valor Inválido!")
    turno = input("digite o seu turno (M-matutino ou V-Vespertino ou N- Noturno): ").lower()
    continue
else:
    if turno == "m":
        print("Bom dia!")
    elif turno == "v":
        print("Boa tarde!")
    else:
        print("Boa noite!")