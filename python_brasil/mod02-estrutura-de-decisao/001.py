""" Faça um Programa que peça dois números e imprima o maior dele """

num1 = int(input('Informe número 01: '))
num2 = int(input('Informe número 02: '))

maior = 0

if num1 > num2:
    maior = num1

else: 
    maior = num2

print(f'O maior número é o {maior}')