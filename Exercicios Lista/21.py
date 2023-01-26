#Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
# Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#O modelo do carro mais econômico;
#Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.
# Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

veiculos = []
kms = []
gasolina = 2.25

for x in range(5):
    veiculo = input(f"Veiculo {x+1}: ")
    km = float(input("Km por litro:"))
    veiculos.append(veiculo)
    kms.append(km)

print("Relatório Final")

for v,k in zip(veiculos, kms):
    kgm = 1000/k
    valor = kgm*gasolina
    print(f"{v}     -   {k:.1f} - {kgm:.1f} litros - R$ {valor:.2f}")

ec = max(kms)
i_ec = kms.index(ec)
economico = veiculos[i_ec]

print(f"O menor consumo é do {economico}")