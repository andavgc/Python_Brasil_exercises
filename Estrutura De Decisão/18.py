#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

#mensagens de output
erro = "Essa data é inválida!"
certo = "A data é valida!"

#pegamos o input do usuario
data = input("digite uma data no formato dd/mm/aaaa: ")

#dividimos a data nos diversos elementos que a conformam:
elementos = data.split("/")
dia = int(elementos[0])
mes = int(elementos[1])
ano = int(elementos[2])

#para definir se o ano é bissexto:
bissexto = False
if ano % 4 == 0:
    bissexto = True

#meses com 31 dias:
mes_longo = [1, 3, 5, 7, 8, 10, 12]

#limpando numeros negativos
if ano or mes or dia < 0:
    print(erro)
#processamento de data (in)valida:
else:
    if ano > 9999:
        print(erro)
    else:
        if mes > 12:
            print(erro)
        #para os meses com 31 dias
        elif mes in mes_longo:
            if dia > 31:
                print(erro)
        #para o mes de fevereiro
        elif mes == 2:
            if bissexto:
                if dia > 29:
                    print(erro)
                else:
                    print(certo)
            else:
                if dia > 28:
                    print(erro)
                else:
                    print(certo)
        #para o resto dos meses
        else:
            if dia > 30:
                print(erro)
            else:
                print(certo)