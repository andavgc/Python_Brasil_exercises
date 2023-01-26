#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas,
#e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

temperaturas = []
temp = True

while temp:
    temperatura = float(input("Informe a temperatura: "))
    temperaturas.append(temperatura)
    cont = ''
    while cont not in ["y", "n"]:
        cont = input("deseja adicionar mais uma temperatura? (y/n): ").lower()
    if cont == "y":
        continue
    if cont == "n":
        temp = False

menor = min(temperaturas)
maior = max(temperaturas)

print(f"A maior temperatura registrada foi {menor}cº e a maior {maior}cº")