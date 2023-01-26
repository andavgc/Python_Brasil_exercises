#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

#pegamos o numero
numero = int(input("digite um número menor a 1000: "))
valores = []
num_real = numero

for i in range(4):
    n = numero % 10
    valores.append(n)
    numero //= 10

u = valores[0]
d = valores[1]
c = valores[2]
m = valores[3]

if c == 1:
    c_txt = "centena"
else:
    c_txt = "centenas"
if d == 1:
    d_txt = "decena"
else:
    d_txt = "decenas"
if u == 1:
    u_txt = "unidade"
else:
    u_txt = "unidades"

if m == 0:
    if c is not 0:
        if d is not 0:
            if u is not 0:
                print("%d = %d %s, %d %s e %d %s" % (num_real, c, c_txt, d, d_txt, u, u_txt))
            if u == 0:
                print("%d = %d %s e %d %s" % (num_real, c, c_txt, d, d_txt))
        if d == 0:
            if u is not 0:
                print("%d = %d %s e %d %s" % (num_real, c, c_txt, u, u_txt))
            if u == 0:
                print("%d = %d %s" % (num_real, c, c_txt))
    if c == 0:
        if d is not 0:
            if u is not 0:
                print("%d = %d %s e %d %s" % (num_real, d, d_txt, u, u_txt))
            if u == 0:
                print("%d = %d %s" % (num_real, d, d_txt))
        if d == 0:
            print("%d = %d %s" % (num_real, u, u_txt))

else:
    print("%d = %d milhar" % (num_real, m))




#unidade
#decena
#centena
#mil



#numero = "{:04}".format(x)