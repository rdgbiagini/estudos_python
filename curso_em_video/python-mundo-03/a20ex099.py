""" Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior. """

from time import sleep

def maior(* num):
    
    cont = 0 
    maior = 0 
    
    print('=' * 50)
    print('\nAnalisando os valores passados... ')
    
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

#  ESSE PRINT ABAIXO ESTÁ DENTRO DA FUNÇÃO. 

    print(f'\nForam informados {cont} valores ao todo. ')
    print(f'O maior valor é {maior}.\n')

#PROGRAMA PRINCIPAL

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 8)
maior(2, 1)
maior(6)
maior(-3, -5, -190)

