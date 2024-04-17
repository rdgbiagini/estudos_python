""" Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a 
segunda função vai mostrar a soma, desses números, que sejam pares. """

# PARA ESSE EXERCÍCIO BAIXAMOS DUAS FUNÇÕES DE BIBLIOTECAS (SLEEP E RANDINT)

from random import randint
from time import sleep

# AQUI COMEÇA A FAZER UMA A UMA AS FUNÇÕES, NESSE CASO JÁ TEMOS 2 FUNÇÕES, MISTURADOS COM CONCEITOS DE LISTAS.
def sorteia(lista):
    print('Sorteando 5 números: (.....)', flush=True)
    sleep(0.3)
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista} nós temos {soma}.')

# A PARTIR DESSE PONTO ESTAMOS ENTRANDO NO PROGRAMA PRINCIPAL. 

numeros = list()
sorteia(numeros)
sleep(0.3)
print(numeros)
somaPar(numeros)