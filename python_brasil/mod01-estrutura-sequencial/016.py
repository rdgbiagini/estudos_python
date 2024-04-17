""" Faça um programa para uma loja de tintas. 

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. """

# BIBLIOTECAS IMPORTADAS

import math

# TAMANHO EM M² A SER PINTADO

area = float(input('Quantos metros quadrados (m²) tem a área a ser pintada? [   ]'))

litrosTinta = math.ceil(area / 3)
latasTinta = math.ceil(litrosTinta / 18) 

# A FUNÇÃO "math.ceil()" FAZ O ARREDONDAMENTO PRA CIMA DAS CONTAS, UMA VEZ QUE ESTAMOS FALANDO DE VALORES FINANCEIROS

# RESULTADO DA QUANTIDADE 

print(f'Considerando que temos {area}m² é necessario {litrosTinta} litros de tinta, que serão atingidas em {latasTinta} latas de tinta a 18 litros cada lata. ')

# PREÇO

preco = latasTinta * 80.00

# RESULTADO FINAL DO PROGRAMA

print(f'Quantidade de latas a serem compradas é {latasTinta}.')
print(f'Preço total é: R$ {preco}')