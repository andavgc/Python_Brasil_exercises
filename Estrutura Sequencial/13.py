#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = input("digite sua altura em metros: ")
test = altura.replace('.','').isdigit()
genero = ""

while test is not True:
    print("por favor digite um número")
    altura = input("digite sua altura: ")
    test = altura.replace('.','').isdigit()
    continue
while "." not in altura:
    print("por favor digite sua altura em metros. exp: 1.63")
    altura = input("digite sua altura: ")
    continue
else:
    altura = float(altura)


genero = input("digite seu gênero (M/F): ").lower()

while "f" not in genero and "m" not in genero:
    print("por favor digite só uma das opções dadas")
    genero = input("digite seu gênero (M/F): ").lower()
    print(genero)
    continue

if genero == "m":
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

print("seu peso ideal é %d kg" % peso_ideal)