import math

litros_lata = 18
litros_galao = 3.6
valor_lata = 80
valor_galao = 25

#usar galao até 0.80, dps adicionar 1 lata

metros = int(input("informe o tamanho da sua casa em m²: "))
litros_necessarios = metros / 6

#se for multiplo de 2 adicionar 1 galao, exceto quando é 5

galoes = litros_necessarios / 3.6

#cada 5 galoes é 1 lata
latas = galoes / 5
latas_necessarias = math.floor(latas)
galoes_necessarios = math.ceil((latas - latas_necessarias) * 5)

valor_lata_final = latas_necessarias * 80
valor_galao_final = galoes_necessarios * 25
valor = valor_lata_final + valor_galao_final

#galoes_necesarios é até 4

if latas_necessarias == 0:
    print("Você precisa comprar %d galões de tinta e deverá pagar R$ %d" % (galoes_necessarios, valor))
elif latas_necessarias > 0:
    print("Você precisa comprar %d latas e %d galões de tinta, e deverá pagar R$ %d" % (latas_necessarias, galoes_necessarios, valor))
