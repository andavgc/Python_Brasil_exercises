#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
#Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
#e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
import random

temperaturas = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for m in range(12):
    t = random.uniform(27.2, 28.1)
    temperaturas.append(t)

media = sum(temperaturas) / len(temperaturas)
print(f"Média anual: {media:.1f}\n")

print("Médias de temperaturas maiores da média anual: ")
for n in temperaturas:
    if n > media:
        i = temperaturas.index(n)
        mes = meses[i]
        print(f"{i+1} - {mes}: {n:.1f}")