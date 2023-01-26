#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro,
#para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso.
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
# Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.

num = 1
codigos = []
alturas = []
pesos = []

cont = True

while cont:
    cod = input(f"{num} - Digite o seu código de academia: ")
    if cod == '0':
        cont = False
        continue
    else:
        altura = float(input("Digite a sua altura em metros: "))
        peso = float(input("Digite o seu peso em kg: "))
        codigos.append(cod)
        alturas.append(altura)
        pesos.append(peso)
        num += 1
        print(codigos)
        print(alturas)
        print(pesos)

#AINDA PRECISA ARRUMAR

#dados do mais alto
altura_alto = max(alturas)
index_alto = alturas.index(altura_alto)
codigo_alto = codigos[index_alto]
peso_alto = pesos[index_alto]

print(f"O usuario mais alto é {codigo_alto}\n",
      f"Altura: {altura_alto} Mts\n",
      f"Peso: {peso_alto} Kg", end='\n\n')

#dados do mais baixo
altura_baixo = min(alturas)
index_baixo = alturas.index(altura_baixo)
codigo_baixo = codigos[index_baixo]
peso_baixo = pesos[index_baixo]

print(f"O usuario mais baixo é {codigo_baixo}\n",
      f"Altura: {altura_baixo} Mts\n",
      f"Peso: {peso_baixo} Kg", end='\n\n')

#dados do mais gordo
peso_gordo = max(pesos)
index_gordo = pesos.index(peso_gordo)
codigo_gordo = codigos[index_gordo]
altura_gordo = alturas[index_gordo]

print(f"O usuario mais pesado é {codigo_gordo}\n",
      f"Altura: {altura_gordo} Mts\n",
      f"Peso: {peso_gordo} Kg", end='\n\n')

#dados do mais magro
peso_magro = min(pesos)
index_magro = pesos.index(peso_magro)
codigo_magro = codigos[index_magro]
altura_magro = alturas[index_magro]

print(f"O usuario mais leve é {codigo_magro}\n",
      f"Altura: {altura_magro} Mts\n",
      f"Peso: {peso_magro} Kg", end='\n\n')

# médias

media_altura = sum(alturas) / len(alturas)
media_peso = sum(pesos) / len(pesos)

print(f"A média de altura da academia é: {media_altura:.2f} mts\n"
      f"A média de peso da academia é: {media_peso:.2f} kg")