""" Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 """

alt = float(input('Informe a altura da pessoa (em metros): [   ]'))
sexo = input('Digite "H" para Homem ou "M" para Mulher: [   ]')

H = (72.7 * alt) - 58
M = (62.1 * alt) - 44.7

if sexo == 'H':
   print(f'O peso ideal é {H}kg')

if sexo == 'M':
    print(f'O peso ideal é {M}kg')