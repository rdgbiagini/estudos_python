""" Faça um programa que leia três números e mostre qual é o maior e qual é o menor entre eles. """

n1 = int(input('PRIMEIRO NÚMERO: '))
n2 = int(input('SEGUNDO NÚMERO: '))
n3 = int(input('TERCEIRO NÚMERO: '))

maior = n1
menor = n1

if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

print(f'O maior é {maior} e o menor foi {menor}')