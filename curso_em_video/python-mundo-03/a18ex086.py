""" Crie um programa que crie uma matriz de dimensão 3x3 e preencha com vários valores lidos pelo teclado (mais precisamente 9 valores, né?) No final mostre a matriz impressa na tela 
com os valores inseridos e de forma organizada, simétrica e limpa na tela. De preferência use cores  """

# UMA MATRIZ DE 3X3 SÃO TRÊS LINHAS (LISTAS) E TRÊS COLUNAS (CONTEÚDOS DESSAS LISTAS)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'DIGITE VALOR PARA [{l}, {c}]: '))

print(matriz)

print('=' * 40)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^7}]', end=' ')
    print('')



