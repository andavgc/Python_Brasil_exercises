#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
# A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 5
#5! =  5 . 4 . 3 . 2 . 1 = 120

num = int(input("insira um numero para calcular seu fatorial: "))
result = 1
fats = []

for x in range(1, num + 1):
    result *= x
    fats.insert(0, str(x))

fats = " . ".join(fats)

print(f"Fatorial de: {num}\n"
      f"{num}! = {fats} = {result}")
