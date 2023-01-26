#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
#O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

#valores

a = int(input("informe o valor de a: "))
while a == 0:
    print("a ecuação não é de segundo grau! ")
    break
else:
    b = int(input("informe o valor de b: "))
    c = int(input("informe o valor de c: "))

#calcular delta

delta = (b**2) - (4*a*c)
print(delta)
if delta < 0:
    print("A ecuação não possui raizes reais")
elif delta == 0:
    x = float(-b/(2*a))
    print("A ecuação possui apenas uma raiz real: %d.2" % x)
else:
    x1 = float((-b + delta) / (2*a))
    x2 = float((-b - delta) / (2 * a))
    print("A ecuação possui duas raizes reais: %.2f e %.2f" % (x1, x2))
