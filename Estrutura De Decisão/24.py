#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

n1 = float(input("primero número: "))
n2 = float(input("primero número: "))
signo = input("Qual operação vc deseja realizar? (+ / - *): ")
frase = []

if "+" in signo:
    resultado = n1 + n2
if "-" in signo:
    resultado = n1 - n2
if "/" in signo:
    resultado = n1 / n2
if "*" in signo:
    resultado = n1 * n2

if resultado > 0:
    pos = "positivo"
elif resultado < 0:
    pos = "negativo"

if resultado == round:
    dec = "inteiro"
elif resultado != round:
    dec = "decimal"

if resultado % 2 == 0:
    par = "par"
elif resultado % 2 != 0:
    par = "impar"

if resultado == 0:
    print("O número é 0")
else:
    print(f"O resultado é {resultado}. O numero é {par}, {pos} e {dec}")