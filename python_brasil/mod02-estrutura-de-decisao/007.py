""" Faça um Programa que leia três números e mostre o maior e o menor deles. """

num1 = int(input('Informe número 01: '))
num2 = int(input('Informe número 02: '))
num3 = int(input('Informe número 03: '))

menor = ()

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3

print(f'O menor número é o {menor}')