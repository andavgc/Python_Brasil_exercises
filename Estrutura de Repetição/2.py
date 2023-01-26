#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

user = input("insira o nome de usuario: ").lower()
senha = input("insira a senha: ").lower()

while user == senha:
    print("A senha não pode ser igual o nome de usuario")
    user = input("insira o nome de usuario: ").lower()
    senha = input("insira a senha: ").lower()

print("Obrigado!")
