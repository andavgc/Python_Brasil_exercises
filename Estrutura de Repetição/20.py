#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

again = True

while again:
    num = -1
    fat = 1
    cont = ''
    while (num < 0) or (num > 16):
        num = int(input("insira um numero entre 0 e 16 para calcular seu fatorial: "))
    else:
        for x in range(1, num + 1):
            fat *= x
        print(fat)
        while cont not in ['y', 'n']:
            cont = input("deseja continuar? (y/n): ")
            if "y" in cont:
                again = True
            if "n" in cont:
                again = False