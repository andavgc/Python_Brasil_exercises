#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

resp = []
s = []

tlf = input('telefonou para a vitima? (s/n): ').lower()
local = input('Esteve no local do crime? (s/n): ').lower()
moradia = input('Mora perto da vítima? (s/n): ').lower()
debito = input('Devia para a vítima? (s/n): ').lower()
trab = input('Já trabalhou com a vítima? (s/n): ').lower()

# organizando respostas

resp.append(tlf)
resp.append(local)
resp.append(moradia)
resp.append(debito)
resp.append(trab)

for x in resp:
    if x == "s":
        s.append(x)

if len(s) < 2:
    print("Inocente")
elif len(s) == 2:
    print("Suspeita")
elif len(s) <= 4:
    print("Cúmplice")
else:
    print("Assasino")

