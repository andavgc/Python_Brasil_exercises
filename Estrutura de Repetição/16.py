#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

fib = int(input("até que série quer gerar a série fibonacci?: "))
num_1 = 0
num_2 = 1
inicial = 1

for x in range(fib):
    if inicial == 1:
        print(inicial, end=" ")
        inicial += 1
    else:
        while x < 500:
            x = num_1 + num_2
            print(x, end=" ")
            num_1 = num_2
            num_2 = x
        else:
            break