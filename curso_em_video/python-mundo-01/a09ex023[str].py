""" Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos:
Ex: Digito o número 1834
4 unidades
3 dezenas
8 centenas
1 milhar

Tentando fazer isso como string e como números """

num = int(input('Digite um número: '))
n = str(num)

print('Analisando o número {num}: ')

print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')