#Altere o programa anterior para mostrar no final a soma dos números.

a = int(input("inserte o primeiro numero: "))
b = int(input("inserte o segundo numero: "))
soma = 0

for x in range((a + 1), b):
    soma += x
    print(x)

print(f"A soma dos numeros é: {soma}")