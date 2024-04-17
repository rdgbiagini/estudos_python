""" Faça um programa que leia o peso de 5 pessoas. 
No final mostre qual foi o maior e o menor peso lidos. """

maior = 0
menor = 0

for p in range(1, 6): 
    peso = float(input(f'{p}º PESO: [   ] '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de \33[32m{maior}\33[m e o menor peso lido foi \33[31m{menor}\33[m.')