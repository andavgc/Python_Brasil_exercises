#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.
#A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50

num = int(input("inserte o numero para saber a tabuada: "))

for x in range(1, 11):
    mult = num * x
    print(f"{num} X {x} = {mult}")