""" Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores. """

def conjunto(n):

    numeros = []
    maior = 0
    menor = 0 
    soma = 0

    for c in range(1, n + 1):
        num = int(input(f'Digite {c}º valor: '))
        numeros.append(num)
        soma += num
        if c == 1:
            maior = num
            menor = num
        elif c > 1:
            if num > maior:
                maior = num
            elif num < menor:
                menor = num
    
    print(f'FORAM INSERIDOS {quant} NÚMEROS.')
    print(f'A LISTA DE NÚMEROS INSERIDOS FOI: {numeros}.')
    print(f'O MENOR VALOR FOI {menor}.')
    print(f'O MAIOR VALOR FOI {maior}.')
    print(f'A SOMA DOS VALORES FOI {soma}.')

quant = int(input('QUANTOS VALORES DESEJA INSERIR? '))
if quant < 1:
    print('ERRO! Informe um valor válido, inteiro, positivo e maior do que 1.')
else:
    conjunto(quant)
    