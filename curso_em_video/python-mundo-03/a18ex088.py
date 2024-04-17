""" Faça um programa que ajude um jogador da mega sena a criar palpites. O programa deverá perguntar quantos jogos serão gerados e vai sortear os 6 números nessa exata quantidade de vezes, 
gerando listas separadas dentro de uma lista grande. 
Importante que o simulador não poderá, dentro de uma mesma lista (de um jogo) sortear 2x o mesmo número. A mega sena vai de 01 a 60..  """

# BIBLIOTECAS

from random import randint
from time import sleep

# LISTAS E INFORMAÇÕES BÁSICAS. O TÍTULO ESTÁ ASSIM, PARA PODER FAZER O PRINT FORMATADO. 

lista = list()
jogos = list()
titulo = 'JOGO DA SENA'
tot = 1

# TÍTULO DE APRESENTAÇÃO.

print()
print('\33[33m=' * 50)
print(f"{titulo:^50}")
print('=' * 50)
print('\33[m')

# PRIMEIRO WHILE. SOBRE QUANTIDADE. 

quant = int(input('QUANTOS JOGOS VOCÊ QUER VER? '))

while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

# PRIMEIRO O SORT FAZ A LISTA FICAR EM ORDEM CRESCENTE. DEPOIS COPIA OS ITENS SEM CONECTAR AS LISTAS E POR FIM LIMPA A LISTA TEMPORÁRIA. 

    lista.sort()
    jogos.append(lista[:])
    lista.clear()

    tot += 1

print('\n', '-=' * 3, f'SORTEANDO {quant} JOGOS: ', '-=' * 3)

for i, l in enumerate(jogos):
    print(f"JOGO {i + 1} : {l} ")
    sleep(0.5)

print(f'OS NÚMEROS FORAM: {jogos} ')
