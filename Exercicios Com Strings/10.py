#Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso

unidade = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
decena = ['zero', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sesenta', 'setenta', 'oitenta', 'noventa']

numero = ''

while numero not in range(0, 100):
    numero = int(input('Insira um número de 0 a 99: '))

numero = str(numero)

if len(numero) == 1:
    dec_ext = ''
    un = int(numero[0])
    num_extenso = unidade[un]
else:
    un = int(numero[1])
    un_ext = unidade[un]
    dec = int(numero[0])
    dec_ext = decena[dec]
    if un == 0:
        num_extenso = dec_ext
    else:
        if numero == '11':
            num_extenso = 'onze'
        elif numero == '12':
            num_extenso = 'doze'
        elif numero == '13':
            num_extenso = 'treze'
        elif numero == '14':
            num_extenso = 'catorze'
        elif numero == '15':
            num_extenso = 'quinze'
        elif numero == '16':
            num_extenso = 'dezesseis'
        elif numero == '17':
            num_extenso = 'dezessete'
        elif numero == '18':
            num_extenso = 'dezoito'
        elif numero == '19':
            num_extenso = 'dezenove'
        else:
            num_extenso = dec_ext + ' e ' + un_ext

print(num_extenso)






