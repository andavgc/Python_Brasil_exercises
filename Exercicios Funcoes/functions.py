import random


def byte_to_mb(dado):
    mb = dado / 1048576
    return mb

def percentual_storage(espaco, espaco_total):
    porc = (espaco * 100) / espaco_total
    return porc

def print_numeros(n):
    for x in range(1, n+1):
        for y in range(x):
            print(f'{x}', end='\t')
        print('')

def print_numeros_ordem(n):
    for x in range(1, n+1):
        for y in range(1, x+1):
            print(f'{y}', end='\t')
        print('')

def somar(a, b, c):
    soma = a + b + c
    return soma

def polarity(n):
    if n > 0:
        return 'P'
    else:
        return 'N'

def SomaImposto(a, b):
    if "%" in a:
        a = a.replace('%', '')
    a = int(a)
    v = ((a+100) * b) / 100
    return v

def conversao_horario(a):
    a = a.split(':')
    h = int(a[0])
    m = int(a[1])
    if (m > 59) or (h > 24):
        return 'Horário inválido'
    else:
        m = str(m)
    if h > 12:
        h = str(h - 12)
        d = 'P.M'
    else:
        h = str(h)
        d = 'A.M'
    hora = h + ':' + m + ' ' + d
    return hora

def ValorPagamento(prestacao, atraso):
    if atraso > 0:
        multa = prestacao * 0.03
        juros = (prestacao * 0.001) * atraso
    else:
        multa = 0
        juros = 0
    valor = prestacao + multa + juros
    return valor

def qtd_digitos(x):
    carateres = len(str(x))
    return carateres

def reverso_numero(x):
    digito = ''
    x = str(x)
    for c in reversed(x):
        digito = digito + c
    digito = int(digito)
    return digito


def formato_data(data):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
             'novembro', 'dezembro']
    date = data.split("/")
    d = date[0]
    mes = int(date[1]) - 1
    m = meses[mes]
    a = date[2]

    data_formatada = f"{d} de {m} de {a}"
    return data_formatada


def retangulo(linha, coluna):
    topo = coluna * "-"
    filler = "+" * (coluna-2)
    corpo = f"|{filler}|\n" * linha
    retangulo = f"{topo}\n{corpo}{topo}"

    return retangulo