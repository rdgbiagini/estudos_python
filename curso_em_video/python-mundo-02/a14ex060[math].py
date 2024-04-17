""" Faça um programa que leia um número qualquer e mostre seu fatorial. """

from math import factorial

n = int(input('DIGITE VALOR: '))

f = factorial(n)
print(f'O fatorial de {n} é {f}')