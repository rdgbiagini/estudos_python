""" Crie um programa que faça o computador jogar com você o clássico pedra, papel e tesoura. """

from time import sleep
from random import randint

jokempo = ['pedra', 'papel', 'tesoura']

computador = randint(0, 2)

print(computador)

print('Vamos jogar um pouco de jokempo [ . . . ]')
sleep(3)
print('JÔ')
sleep(2)
print('KEN')
sleep(2)
print('PO')
sleep(2)

jogador = int(input('''Escolha: 
    [ 1 ] PEDRA
    [ 2 ] PAPEL
    [ 3 ] TESOURA [ . . . ] 
    
    >>>>>>>>>> [   ] '''))

sleep(2)

if jogador == 1 and computador == 0:
    print('empataram, babacas!')
elif jogador == 1 and computador == 1:
    print('você perdeu! ')
elif jogador == 1 and computador == 2:
    print('\33[1;30;41mvocê ganhou! Parabéns, seu otário.\33[m ')
elif jogador == 2 and computador == 0:
    print('\33[1;30;41mvocê ganhou! Parabéns, seu otário.\33[m ')
elif jogador == 2 and computador == 1:
    print('empataram, babacas!')
elif jogador == 2 and computador == 2:
    print('você perdeu!')
elif jogador == 3 and computador == 0:
    print('\33[1;30;41mvocê ganhou! Parabéns, seu otário.\33[m')
elif jogador == 3 and computador == 1:
    print('empataram, babacas! ')
elif jogador == 3 and computador == 2:
    print('você perdeu! ')