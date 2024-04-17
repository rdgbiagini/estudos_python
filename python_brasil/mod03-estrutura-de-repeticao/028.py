""" Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um. """

# ==================================================================================================================================================================================== #
# BIBLIOTECAS, VARIÁVEIS GLOBAIS, CONTADORES E DEMAIS INFORMAÇÕES PERTINENTES. 
# ==================================================================================================================================================================================== #

somaCDs = 0 

# ==================================================================================================================================================================================== #
# PRIMEIRO QUERO SABER QUANTOS CDS, PORQUE ISSO VAI GERAR O LAÇO FOR NECESSÁRIO. 
# ==================================================================================================================================================================================== #

qCDs = int(input('Quantos CDs: '))

for c in range(1, qCDs + 1):

    pCDs = int(input(f'Qual o valor do {c}ª CD? '))
    somaCDs += pCDs

mediaCDs = somaCDs / qCDs

print(f'Temos um total de {qCDs} CDs, com um preço médio de {mediaCDs} por CD.')