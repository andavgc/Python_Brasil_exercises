#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

a = int(input("Insira a população do país A: "))
taxa_a = int(input("Insira a taxa anual de crescimento do país A (%): "))
b = int(input("Insira a população do país B: "))
taxa_b = int(input("Insira a taxa anual de crescimento do país B (%): "))
anos = 0

perc_a = (taxa_a * 0.01) + 1
perc_b = (taxa_b * 0.01) + 1

if a > b:
    if taxa_a >= taxa_b:
        print("A população do país B nunca vai alcançar a população do país A")
    else:
        while a > b:
            a *= perc_a
            b *= perc_b
            anos += 1
        a = int(a)
        b = int(b)
        print(f"Demorará {anos} anos para a população do país B ({b}) alcançar ou ultrapassar a população do país A ({a})")

elif b > a:
    if taxa_b >= taxa_a:
        print("A população do país A nunca vai alcançar a população do país B")
    else:
        while b > a:
            a *= perc_a
            b *= perc_b
            anos += 1
        a = int(a)
        b = int(b)
        print(f"Demorará {anos} anos para a população do país A ({a}) alcançar ou ultrapassar a população do país B ({b})")
