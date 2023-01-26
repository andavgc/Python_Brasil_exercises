#Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
#Maior e Menor Acerto;
#Total de Alunos que utilizaram o sistema;
#A Média das Notas da Turma.
#Gabarito da Prova:
#01 - A
#02 - B
#03 - C
#04 - D
#05 - E
#06 - E
#07 - D
#08 - C
#09 - B
#10 - A
#Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

gabarito = []
respostas = {}
correcao = True

#gabarito
print("Por favor preencha o gabarito para começar.")
for g in range(10):
    r = input(f"insira a resposta da pergunta nº{g+1}: ").lower()
    gabarito.append(r)

#validacao
while correcao:
    num = 0
    aluno = input("Insira o seu nome: ")
    respostas[aluno] = 0
    for q in range(10):
        resp = ""
        while resp not in gabarito:
            resp = input(f"Insira a resposta da pergunta nº {num + 1}: ").lower()
        if resp == gabarito[num]:
            respostas[aluno] += 1
        num += 1

    continuar = ""
    while continuar not in ["y", "n"]:
        continuar = input("Outro aluno irá utilizar o sistema? (y/n): ").lower()

    if continuar == "n":
        correcao = False

#alunos que usaram o sistema
print(f"Um total de {len(respostas)} alunos usaram o sistema")

#media
media = sum(respostas.values()) / len(respostas.values())
print(f"A media da turma foi {media}")

#maior e menor notas
maior_nota = max(respostas.values())
menor_nota = min(respostas.values())
maior = []
menor = []
i = 0

for a in respostas.values():
    if a == maior_nota:
        aluno_maior = list(respostas.keys())[i]
        maior.append(aluno_maior)
    if a == menor_nota:
        aluno_menor = list(respostas.keys())[i]
        menor.append(aluno_menor)
    i += 1

print(f"A maior nota é de {', '.join(maior)}: {maior_nota} pts")
print(f"A menor nota é de {', '.join(menor)}: {menor_nota} pts")