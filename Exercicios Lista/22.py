#Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área.
#A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
#Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo:
#um número de identificação do mouse o tipo de defeito:
#necessita da esfera;
#necessita de limpeza;
#Necessita troca do cabo ou conector;
#Quebrado ou inutilizado
# Uma identificação igual a zero encerra o programa.
#Ao final o programa deverá emitir o seguinte relatório:
qtd = 0
continuar = True
defeitos = [0, 0, 0, 0]
n_defeitos = ["necessita da esfera", "necessita de limpeza", "necessita troca do cabo ou conector", "quebrado ou inutilizado"]

while continuar:
    id = int(input("Identifique o mouse: "))
    if id == 0:
        continuar = False
        break
    else:
        qtd += 1
        defeito = 0
        while defeito not in [1,2,3,4]:
            print("1 - Necessita da esfera\n"
                    "2 - Necessita de limpeza\n" 
                    "3 - Necessita troca do cabo ou conector\n" 
                    "4 - Quebrado ou inutilizado")
            defeito = int(input("Informe o tipo de defeito:"))
        #contar os defeitos
        else:
            if defeito == 1:
                defeitos[0] += 1
            elif defeito == 2:
                defeitos[1] += 1
            elif defeito == 3:
                defeitos[2] += 1
            elif defeito == 4:
                defeitos[3] += 1
    print(qtd)
    print(defeitos)

#porcentagem
porcentagens = []
for x in defeitos:
    try:
        porc = (x*100)/qtd
    except:
        porc = 0
    porcentagens.append(porc)

print("Situação\t\t\t\t\t\t\t\tQuantidade\t\t\tPercentual")
n = 0
for (x,y,z) in zip(n_defeitos, defeitos, porcentagens):
    print(f"{n}- {x:}\t\t\t{y}\t\t\t{z:.2f}%")
    n += 1