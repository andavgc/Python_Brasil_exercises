#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
#Os códigos utilizados são:
#1 , 2, 3, 4  - Votos para os respectivos candidatos
#(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco
#Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

votacao = True
num = 1
voto = ""
votos = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}
candidatos = ["Andrés", "Alfredo", "Paulo", "Thiago", "Voto em branco", "Voto nulo"]

#lista de candidatos
print("Lista de candidatos: ")
for c in candidatos:
    print(f"{num} - {c}")
    num += 1
print("")

#Processo de votação
while votacao:
    print("Para ver a lista de candidatos, aperte 'c'")
    print("Para encerrar a votação, aperte '0'")
    voto = input("Voto: ").lower()
    #lista de candidatos
    if voto == "c":
        print("Candidatos: ")
        for c in candidatos:
            print(f"{num} - {c}\n")
            num += 1
    #contagem de votos
    elif voto in votos:
        votos[voto] += 1
    elif voto == "0":
        votacao = False
        break

#resultados
print("Resultados: ")
for (c, v) in zip(candidatos, votos.values()):
    print(f"{c}: {v} votos")