#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
#se digitar outro valor deve aparecer valor inválido.

semana = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"]
dias = [0, 1, 2, 3, 4, 5, 6]

dia = int(input("digite um número correspondente ao dia da semana (1-Domingo, 2-Segunda, etc): ")) - 1

while dia not in dias:
    dia = int(input("valor inválido, digite um número de 1 a 7: "))

print(semana[dia])