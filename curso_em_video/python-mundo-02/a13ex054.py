""" Crie um programa que leia o ano de nascimento de 7 pessoas. 
No final mostre quantas pessoas não atingiram a maioridade e quantos já são maiores. """

from datetime import date

hoje = date.today().year

n = int(input('Quantos anos deve informar? RECOMENDADO FAZER COM AO MENOS 7 DIFERENTES. '))

maiores = 0
menores = 0

for y in range(1, n + 1):
    ano = int(input(f'DIGITE {y}º ANO DE NASCIMENTO: '))
    if hoje - ano <= 18:
        menores += 1
    else:
        maiores += 1
print(f'Temos então \33[32m{maiores}\33[m maiores e \33[31m{menores}\33[m menores.')