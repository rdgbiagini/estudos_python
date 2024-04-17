""" Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem. """

n1 = int(input('BASE: '))
n2 = int(input('EXPOENTE: '))

calc = n1 ** n2

print(f'Para a base {n1} e expoente {n2} temos a potência de {calc}.')

