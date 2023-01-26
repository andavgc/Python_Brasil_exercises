#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

primo = True

num = int(input("insira um numero: "))
div = []

for x in range(1, num):
    resto = num % x
    if resto == 0 and num != x and num != 1:
        primo = False
        div.append(str(x))

if primo:
    print("É um número primo")
else:
    print("Não é um numero primo, ele é divisivel por ele mesmo, {}".format(", ".join(div[:-1]) + " e " + div[-1] if len(div) > 1 else "".join(div)))