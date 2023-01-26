#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
#O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
#Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

num = int(input("insira um numero: "))
primos = []
div = 0

for x in range(1, num + 1):
    primo = True
    for z in range(1, x + 1):
        resto = x % z
        div += 1
        if resto == 0 and (z != x) and (z != 1):
            primo = False
    if primo:
        primos.append(str(x))

print(f"Números primos de 1 a {num}: " + "{}".format(", ".join(primos[:-1]) + " e " + primos[-1] if len(primos) > 1 else "".join(primos)))
print(f"foram {div} divisões feitas")
#else:
 #   print("Não é um numero primo, ele é divisivel por ele mesmo, {}".format(", ".join(div[:-1]) + " e " + div[-1] if len(div) > 1 else "".join(div)))