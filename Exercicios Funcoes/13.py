#Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
#Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.
#Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
import functions

linha = input('Informe o valor das linhas do retângulo: ')
coluna = input('Informe o valor das colunas do retángulo: ')

if linha == "":
    linha = 1
if coluna == "":
    coluna = 1
elif linha not in range(1, 21):
    linha = 20
elif coluna not in range(1,21):
    coluna = 20

linha = int(linha)
coluna = int(coluna)
l = functions.retangulo(linha, coluna)

print(l)