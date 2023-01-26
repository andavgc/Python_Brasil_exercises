#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
#F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Qual é seu sexo? (M/F): ").lower()

if "f" in sexo:
    print("É feminino")
elif "m" in sexo:
    print("É masculino")
else:
    print("sexo inválido")