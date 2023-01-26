#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
numeros = []

for num in range(5):
    num = int(input("inserte um numero de 1 a 1000: "))
    while num < 0 or num > 1000:
        num = int(input("número inválido, insira numeros de 1 a 1000 unicamente: "))
    else:
        numeros.append(num)

min = min(numeros)
max = max(numeros)
sum = sum(numeros)

print(f"menor numero: {min}, maior numero: {max}, soma dos numeros: {sum}")