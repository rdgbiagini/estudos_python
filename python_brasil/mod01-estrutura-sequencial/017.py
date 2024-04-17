""" Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, 
isto é, considere latas cheias. """

import math

# TAMANHO EM METROS QUADRADOS DA ÁREA A SER PINTADA

area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

# CÁLCULO DA QUANTIDADE DE TINTA NECESSÁRIA EM LITROS (COM 10% A MAIS)

litrosTinta = math.ceil((area / 6) * 1.1)

# CÁLCULO DA QUANTIDADE DE LATAS E GALÕES
# LEMBRANDO QUE O "math.ceil()" FAZ O ARREDONDAMENTO DAS CONTAS PRA CIMA

latasTintas = math.ceil(litrosTinta / 18) # CADA LATA TEM 18 LITROS
galoesTintas = math.ceil(litrosTinta / 3.6) # CADA GALÃO TEM 3.6 LITROS

# CÁLCULO DOS PREÇOS

precoLatas = latasTintas * 80.00
precoGaloes = galoesTintas * 25.00

# CÁLCULO DA QUANTIDADE DE LATAS E GALÕES MISTURADOS
# NO SEGUNDO CÁLCULO ARREDONDA PRA CIMA 

latasMisturadas = int(litrosTinta / 18) 
galoesMisturados = math.ceil((litrosTinta % 18) / 3.6)

precoMisturados = math.ceil((litrosTinta % 18) / 3.6)

# CÁLCULO DO PREÇO FINAL 

preco = (latasMisturadas * 80.00) + (galoesMisturados * 25.00)

# RESULTADOS FINAIS
print("Quantidades a serem compradas:")
print(f"Latas de tinta de 18 litros: {latasTintas}")
print(f"Galões de tinta de 3,6 litros: {galoesTintas}")

print("Preços:")
print(f"Preço apenas com latas de 18 litros: R$ {precoLatas:.2f}")
print(f"Preço apenas com galões de 3,6 litros: R$ {precoGaloes:.2f}")
print(f"Preço misturando latas e galões: R$ {precoMisturados:.2f}") ################