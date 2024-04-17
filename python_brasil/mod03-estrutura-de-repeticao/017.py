""" Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 """

def fatorial(n):
    if n == 0:
        return 1
    else: 
        return n * fatorial(n-1)

n = int(input('DIGITE VALOR A SER CALCULADO SEU FATORIAL: '))

if n < 0:
    print('ERRO!')
else:
    resultado = fatorial(n)
    print(f'O fatorial de {n} é {resultado}.')