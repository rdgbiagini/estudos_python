""" Crie um programa que vai gerar 5 números aleatórios e coloque dentro de uma tupla nova. Depois mostre a listagem de números gerados e indique quais foram o maior e 
o menor números sorteados e incluídos nessa tupla.  """

from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

for n in numeros:
    print(f'{n}', end=' ')


print(f'\nO maior número foi o {max(numeros)}.  ')
print(f'O menor número foi {min(numeros)}.  ')