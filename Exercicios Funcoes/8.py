#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
import functions

num = int(input('Insira um número: '))

carateres = functions.qtd_digitos(num)

print(f'O número tem {carateres} dígitos.')