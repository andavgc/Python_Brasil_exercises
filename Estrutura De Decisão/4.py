#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal = ["a", "e", "i", "o", "u"]
letra = input("digite uma letra: ")
flag_letra = True

while flag_letra:
    if letra.isdigit() is True:
        flag_letra = False
        print("por favor digite uma letra válida")
        letra = input("digite uma letra: ")
    elif letra in vogal:
        print("A letra é uma vogal")
        break
    else:
        print("A letra é uma consoante")
        break
    flag_letra = True