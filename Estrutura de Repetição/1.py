#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = ""

while nota not in range(11):
    nota = int(input("insira uma nota de zero a dez: "))

print(f"A nota é {nota}")