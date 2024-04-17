""" Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos:
Ex: Digito o número 1834
4 unidades
3 dezenas
8 centenas
1 milhar

Tentando fazer isso como string e como números """

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {num}: ')

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
