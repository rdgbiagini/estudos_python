""" Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. """

# CONTADOR PARA SABER A QUANTIDADE DE NÚMEROS PELOS QUAIS O "n" É DIVISÍVEL PARA DEFINIR SE ELE É PRIMO OU NÃO. 

tot = 0

n = int(input('DIGITE UM NÚMERO INTEIRO: [   ] '))

# LAÇO "for" PARA DEFINIR A DIVISÃO DO NÚMERO POR TODOS OS NÚMEROS ATÉ ELE MESMO, PARA ENCONTRAR QUAIS SERIAM APENAS DIVISÍVEIS POR 1, 3 E ELE MESMO.

for c in range(1, n + 1):
    if n % c == 0:
        print(f'\33[33m', end=' ')
        tot += 1
    else: 
        print(f'\33[31m', end=' ')
    print(c, end=' --> ')
print(f'\n\33[m' + f'O número {n} foi divisível \33[34m{tot}\33[m vezes.')

# ESSE "if" É FORA DO LAÇO PRA PODER AJUSTAR SE O CABRA É PRIMO OU NÃO. O LAÇO ACIMA É SÓ PARA DEFINIR AS DIVISÕES APENAS. 

if tot == 2:
    print('E por isso ele \33[1;35mÉ PRIMO\33[m.')
else:
    print('E por isso ele \33[1;31mNÃO É PRIMO\33[m.')

print('FIM')

# O MEU ERRO NESSE CÓDIGO FOI TENTAR ENTENDER, QUAIS ERAM OS NÚMEROS PRIMOS DENTRO DE UM RANGE, ENQUANTO ELE QUERIA SABER SE O NÚMERO DADO ERA PRIMO APENAS.