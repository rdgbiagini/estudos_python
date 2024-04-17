""" Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. """

ano = float(input('Informe um ano: '))

if ano % 4 == 0:
    print('Sim, é um ano bissexto.')
else:
    print('Não é um ano bissexto.')

#Tive que lembrar do "resto da divisão" mas realmente é um calculo simples.
#Se um número for divisível por outro, o "resto" dessa divisão será sempre zero, então para todo o resto, não é divisível. 