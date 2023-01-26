salarios = []
abonos = []
continuar = True
valor = 1
colab = 0
minimo = 0

while continuar:
    if valor >= 0:
        valor = int(input("Salário: "))
        if valor == 0:
            continuar = False
            break
        else:
            salarios.append(valor)
            abono = valor * 0.2
            if abono < 100:
                abonos.append(100)
                minimo += 1
            else:
                abonos.append(abono)
            colab += 1

print("Salário - Abono")
for (x, y) in zip(salarios, abonos):
    print(f"R${x} - R${y}")

print(f"foram processados {colab} colaboradores")
print(f"total gasto com abonos: R${sum(abonos)}")
print(f"Valor mínimo pago a {minimo} colaboradores")
print(f"Maior Valor de abono pago: R${max(abonos)}")