#Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

#Data de Nascimento: 29/10/1973
#Você nasceu em  29 de Outubro de 1973.

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro']

data = input("Insira sua data de nascimento no formato DD/MM/AAAA: ")

date = data.split("/")
d = date[0]
mes = int(date[1]) - 1
m = meses[mes]
a = date[2]

print(f"Você nasceu em {d} de {m} de {a}")