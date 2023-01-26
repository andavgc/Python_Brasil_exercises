numeros = [1,2,3,4,5,6,7,8,9]
combinacoes = []

for a in numeros:
    for b in numeros:
        for c in numeros:
            if a+b+c==15:
                if (a != b != c):
                    combinacoes.append([a, b, c])

for l1 in combinacoes:
    for l2 in combinacoes:
        if (l2[0] == l1[0]) or (l2[1] == l1[1]) or (l2[2] == l1[2]) or (l2[1] == l1[0]) or (l2[1] == l1[2]):
            pass
        for l3 in combinacoes:
            if (l3[0] == l2[0]) or (l3[1] == l2[1]) or (l3[2] == l2[2]) or (l3[0] == l1[0]) or (l3[1] == l1[1]) or (l3[2] == l1[2]) or (l3[0] == l2[1]) or (l3[2] == l2[1]):
                pass
            else:
                if (l1[0] + l2[0] + l3[0] == 15) and (l1[1] + l2[1] + l3[1] == 15) and (l1[2] + l2[2] + l3[2] == 15) and (l1[0] + l2[1] + l3[2] == 15) and (l1[2] + l2[1] + l3[0] == 15):
                    print(f'{l1}\n{l2}\n{l3}\n')







