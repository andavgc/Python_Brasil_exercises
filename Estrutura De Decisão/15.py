#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

a = int(input("digite o tamanho do primeiro lado: "))
b = int(input("digite o tamanho do segundo lado: "))
c = int(input("digite o tamanho do terceiro lado: "))

if a + b > c and a + c > b and c + b > a:
    if a == b == c:
        print("É um triângulo equilátero")
    elif a == b or b == c or a == c:
        print("É um triângulo isósceles")
    else:
        print("É um triângulo escaleno")
else:
    print("Não é um triângulo!")
