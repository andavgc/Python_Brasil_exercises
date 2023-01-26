from Python_Brasil import functions

nomes = []
memorias = []

#abrir o arquivo recebido
u = open('usuarios.txt')
#separar e distribuir os nomes e a memoria utilizada nas listas acima
for n in u.readlines():
    nome = n.split()[0]
    byte = n.split()[1]
    memoria = functions.byte_to_mb(int(byte))
    nomes.append(nome)
    memorias.append(memoria)

#calcular a memoria total e a média de memoria utilizada
memoria_total = sum(memorias)
media = sum(memorias) / len(memorias)

#textos para gerar o novo arquivo
cabecal = 'ACME Inc.\t\t\t Uso do espaço em disco pelos usuários'
titulo_1 = 'Nr.'
titulo_2 = 'Usuário'
titulo_3 = 'Espaço Utilizado'
titulo_4 = '% do uso'

#criar e modificar o novo arquivo
with open('relatorio.txt', 'w') as relatorio:
    relatorio.write(cabecal + '\n')
    relatorio.write('------------------------------------------------------------------------\n')
    relatorio.write(titulo_1 + '  ' + titulo_2 + '\t\t' + titulo_3 + '\t' + titulo_4 + '\n')
    num = 1
    #pegar os dados das listas e distribuir no arquivo novo
    for (x,y) in zip(memorias, nomes):
        #calcula porcentagem que cada memoria ocupa em relação ao total
        porc = functions.percentual_storage(x, memoria_total)
        #criando uma lista com os dados de cada usuário já estruturados
        data = list((y, str('{:.2f}'.format(x)) + ' MB', str('{:.2f}'.format(porc)) + '%'))
        #substituir os pontos por virgulas
        data[1] = data[1].replace('.', ',')
        data[2] = data[2].replace('.', ',')
    #formatar os dados no arquivo
        relatorio.write('{:<5}'.format(str(num)) + '{:<19}'.format(data[0]) + '{:>15}'.format(data[1]) + '{:>15}'.format(data[2]) + '\n')
        num += 1
    memoria_total = str(f'{memoria_total:.2f}').replace('.', ',')
    media = str(f'{media:.2f}').replace('.', ',')
    relatorio.write(f'\nEspaço total ocupado: {memoria_total} MB\nEspaço médio ocupado: {media} MB')
relatorio.close()

with open('relatorio.txt', 'r') as relatorio:
    print(relatorio.read())
relatorio.close()
