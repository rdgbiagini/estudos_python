""" Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e depois realize uma contagem com base nesses dados. Seu programa tem 
que realizar três contagens através da função criada: 01 - De a até 10, de 1 em 1 / 02 - De 10 até 0, de 2 em 2 / 03 - Uma contagem personalizada. """

from time import sleep
def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}.')
    sleep(2)

    if passo < 0:
        p *= -1
    elif passo == 0:
        passo = 1

    if inicio < fim: 
        cont = inicio
        while cont <= fim:
            print(cont, end=' ', flush=True)
            sleep(0.3)
            cont += passo
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ', flush=True)
            sleep(0.3)
            cont -= passo

        print('FIM')

# PROGRAMA PRNCIPAL

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez: ')
i = int(input('INÍCIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))

contador(i, f, p)