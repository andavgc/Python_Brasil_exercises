#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("insira seu nome: ")
while (len(nome) <= 3) or "":
    nome = input("nome inválido, por favor insira um nome com mais de 3 caracteres: ")

idade = int(input("insira sua idade: "))
while (0 > idade) or (idade > 150) or "":
    idade = int(input("idade inválida, por favor insira uma idade de 0 a 150: "))

salario = int(input("Insira seu salario em R$: "))
while (0 > salario) or "":
    salario = int(input("salário inválido, por favor insira um valor maior a 0: "))

sx = ["f", 'm']
sexo = input("Qual é seu sexo? (f/m): ").lower()
while (sexo not in sx) or "":
    sexo = input("sexo inválido, por favor insira um valor entre as opções (f/m): ").lower()

ev = ["s", "c", "v", "d"]
estado_civil = input("Qual é seu estado civil? [(s)olteiro/a, (c)asado/a, (v)iuvo/a, (d)ivorciado/a]: ").lower()
while (estado_civil not in ev) or "":
    estado_civil = input("Estado civil inválido, por favor insira um valor entre as opções [(s)olteiro/a, (c)asado/a, (v)iuvo/a, (d)ivorciado/a]: ").lower()

print("Obrigado!")