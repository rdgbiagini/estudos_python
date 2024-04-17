""" Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
A) o produto do dobro do primeiro com metade do segundo .
B) a soma do triplo do primeiro com o terceiro.
C) o terceiro elevado ao cubo. """

num1 = int(input('Informe número 01: '))
num2 = int(input('Informe número 02: '))
num3 = float(input('Informe número 03: '))

calc1 = (2 * num1) + (num2 / 2)
calc2 = (3 * num1) + num3
calc3 = (num3 * num3 * num3)

print(calc1)
print(calc2)
print(calc3)
