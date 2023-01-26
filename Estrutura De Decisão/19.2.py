# numero = int(input("insira um numero de 1 a 1000: "))
#
# u = ''
# d = ''
# c = ''
# m = ''
#
# for i in range(3):
#     i = numero % 10
#         if len(i) == 1
#

str1 = str2 = str3 = str4 = ""
numero = int(input("insira um numero de 1 a 1000: "))


numero = numero // 10
if numero % 10 > 0:
    str3 = f"{numero % 10} centenas "

numero = numero // 10
if numero % 100 > 0:
    str2 = f"{numero % 100} dezenas "

numero = numero // 10
if numero % 1000 > 0:
    str1 = f"{numero % 1000} unidades"

print(str4 + str3 + str2 + str1)