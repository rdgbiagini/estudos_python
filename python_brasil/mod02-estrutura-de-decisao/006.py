""" Faça um Programa que leia três números e mostre o maior deles. """

num1 = int(input('Informe número 01: '))
num2 = int(input('Informe número 02: '))
num3 = int(input('Informe número 03: '))

maior = ()

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

print(f'O maior número é o {maior}')