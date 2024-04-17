""" Faça um programa que leia um número qualquer e mostre seu fatorial. """

n = int(input('DIGITE VALOR: '))

c = n
f = 1 
print(f'CALCULANDO O {n}! = ', end=' ')
while c >= 1:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print(f'\nO fatorial de {n} é {f}')