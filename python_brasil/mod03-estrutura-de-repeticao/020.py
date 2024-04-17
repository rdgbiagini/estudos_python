""" Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16. """

def fatorial(n):
    if n == 0:
        return 1
    elif n > 0 and n < 16:
        return n * fatorial(n-1)
    else:
        print('\33[31mERRO! DIGITE APENAS VALORES ENTRE 1 E 16.\33[31m')
        

n = int(input('DIGITE VALOR PARA SER CALCULADO SEU FATORIAL: '))

if n < 0:
    print('ERRO!')
else:
    resultado = fatorial(n)
    print(f'O fatorial de {n} é {resultado}.')
    