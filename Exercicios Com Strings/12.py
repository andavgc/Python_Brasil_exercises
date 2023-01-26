#Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos,
#acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

tlf = input('insira um número de telefone: ')

if '-' in tlf:
    if len(tlf) < 9:
        tlf2 = '3' + tlf
        tlf1 = tlf.replace('-', '')

else:
    if len(tlf) < 8:
        tlf1 = '3' + tlf
        tlf2 = list(tlf1)
        tlf2.insert(4, "-")
        tlf2 = ''.join(tlf2)

print(f'Telefone corrigido sem formatação: {tlf1}')
print(f'Telefone corrigido com formatação: {tlf2}')