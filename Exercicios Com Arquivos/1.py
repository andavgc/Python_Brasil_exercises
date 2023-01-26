#Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
#contendo um relatório dos endereços IP válidos e inválidos.
validas = []
invalidas = []

data = open("ip.txt", "r")

#validacao
for ip in data.readlines():
    ip = ip.replace("\n", "")
    ip = ip.split(".")
    print(ip)
    for numero in ip:
        print(numero)
        if int(numero) >= 255:
            invalidas.append(".".join(ip))
            pass
    if ip not in invalidas:
        validas.append(".".join(ip))
data.close()

print(validas)
print(invalidas)

validacao = open("validacao.txt", "w")

validacao.write("[Endereços válidos:]\n")

for ip in validas:
    validacao.write(ip + "\n")

validacao.write("\n[Endereços inválidos:]\n")

for ip in invalidas:
    validacao.write(ip + "\n")

validacao.close()

r = open("validacao.txt", "r")

print(r.read())

validacao.close()