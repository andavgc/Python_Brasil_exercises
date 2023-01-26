#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
#Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;

valores = []
continuar = True

while continuar:
    valor = -2
    while valor < -1:
        valor = int(input("Insira um valor igual ou maior a 0: "))
    if valor == -1:
        continuar = False
        break
    elif valor > 0:
        valores.append(valor)

qtd = len(valores)
print(f"valores lidos: {qtd}")

print("valores:", end=' ')
for v in valores:
    print(v, end=' ')
print("\n")

print("valores ao contrario: ")
for v in reversed(valores):
    print(v)

soma = sum(valores)
print(f"soma dos valores: {soma}")

media = soma / qtd
print(f"media dos valores: {media:.2f}")

print("valores acima da media:", end=' ')
for n in valores:
    if n > media:
        print(n, end=' ')
print('\n')

print("valores abaixo de 7:", end=' ')
for n in valores:
    if n < 7:
        print(n, end=' ')

print("Programa encerrado.")