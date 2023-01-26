# Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
# indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.
invalido = "O CPF inserido não é um CPF válido"
validez = True
cpf = input("Insira seu CPF no formato xxx.xxx.xxx-xx: ")

cpf_inicio = cpf[0:11].replace(".", "")
dfs = cpf[-2:]

for x in range(2):
    # verificação dos numeros verificadores
    numeros = []
    mult = len(cpf_inicio) + 1

    for numero in cpf_inicio:
        y = int(numero) * mult
        numeros.append(y)
        mult -= 1

    # somar os resultados de numeros
    multiplicando = sum(numeros)
    # Pegar o resto da divisão do numero por 11
    resto = multiplicando % 11

    dv2 = ''
    if resto in [0, 1]:
        dv2 = '0'
    elif resto in range(2, 11):
        dv2 = str(11 - resto)

    df = dfs[x]
    if dv2 != df:
        print(invalido)
        validez = False
        break
    else:
        cpf_inicio += df

if validez:
    print('O CPF é válido')