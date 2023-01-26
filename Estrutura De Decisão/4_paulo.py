#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal = ["a", "e", "i", "o", "u"]

while True:
    letra = input("digite uma letra: ")
    if letra.isdigit():
        print("por favor digite uma letra válida")
    elif letra in vogal:
        print("A letra é uma vogal")
        break
    else:
        print("A letra é uma consoante")
        break
