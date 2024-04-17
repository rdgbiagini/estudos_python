""" Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento. """

num = float(input('Digite um valor.'))
round(num)

if round(num) == num:
    print('Esse número é inteiro.')
else:
    print('Esse número não é inteiro.')