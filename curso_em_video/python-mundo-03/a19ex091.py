""" Crie um programa aonde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados todos em um dicionário. No final, 
coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado. """

from random import randint; from time import sleep; from operator import itemgetter

total = list()
jogo = dict()
ranking = list()

for j in range(1, 5):
    jogo[f'Jogador {j}'] = randint(1,6)

# NESSE PONTO AQUI, EU AINDA FIZ ATRAVÉS DE UM "for" ENQUANTO O GUANABARA FEZ UM A UM COMO VOU ESCREVER ABAIXO:

"""
jogo = {'jogador 1' : randint(1, 6),
        'jogador 2' : randint(1, 6),
        'jogador 3' : randint(1, 6),
        'jogador 4' : randint(1, 6)}

"""

print('VALORES SORTEADOS: ')

for k, v in jogo.items():
    print(f'{k} tirou {v}.')
    sleep(0.5)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i - 1}º LUGAR: {v[0]} com {v[1]}.')
    sleep(0.5)


