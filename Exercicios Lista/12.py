#Foram anotadas as idades e alturas de 30 alunos.
#Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
import random

I = []
A = []
menores = 0

for a in range(30):
    n = random.randint(6, 17)
    m = random.uniform(1.20, 1.90)
    I.append(n)
    A.append(float(f"{m:.2f}"))

media_altura = sum(A) / len(A)
print(f"{media_altura:.2f}")

for i in I:
    if i > 13:
        aluno = I.index(i)
        altura = A[aluno]
        if altura < media_altura:
            menores += 1
            print(i, altura)

print(f"tem {menores} alunos com mais de 13 anos com altura menor à média")