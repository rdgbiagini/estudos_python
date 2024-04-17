""" Faça um programa que leia um ano e mostre se ele é um ano bissexto. """

ano = int(input('DIGITE UM ANO: '))

if ano % 4 == 0 and ano % 400 == 0 and ano % 100 != 0:
    print('É um ano bissexto.')
else:
    print('Não é um ano bissexto.')