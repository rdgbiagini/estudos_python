""" Aprimore o desafio anterior, mostrando agora: 01 - A soma de todos os valores pares digitados / 02 - A soma dos valores da terceira coluna / 03 - O maior valor da segunda linha / 
04 - a soma de todos os valores / 05 - A multiplicação entre o primeiro e o último valor digitado.  """

# UMA MATRIZ DE 3X3 SÃO TRÊS LINHAS (LISTAS) E TRÊS COLUNAS (CONTEÚDOS DESSAS LISTAS)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = 0
somaImpares = 0
somaTodos = 0 
somaColuna2 = 0
maiorSegundaLinha = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'DIGITE VALOR PARA [{l}, {c}]: '))
        somaTodos += matriz[l][c]
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
        else:
            somaImpares += matriz[l][c]
            
for l in range(0, 3):
    somaColuna2 += matriz[l][2]

print(matriz)

for c in range(0, 3):
    if c == 0:
        maiorSegundaLinha = matriz[1][c]
    elif matriz[1][c] > maiorSegundaLinha:
        maiorSegundaLinha = matriz[1][c]

print('=' * 40)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^7}]', end=' ')
    print('')

print(f'SOMA DOS PARES: {somaPares} ')
print(f'SOMA DOS IMPARES: {somaImpares} ')
print(f'SOMA DA 3ª COLUNA: {somaColuna2}')
print(f'A SOMA DE TODOS É: {somaTodos} ')
print(f'O MAIOR DA SEGUNDA LINHA É: {maiorSegundaLinha}')

