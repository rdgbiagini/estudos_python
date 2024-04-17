""" Escreva um programa que faça o computador pensar em um número de 0 a 5 e peça para o jogador tentar adivinhar o número pensado. 
O programa deverá escrever na tela se o usuário venceu ou perdeu. """

from random import randint
from time import sleep

c = randint(0, 5)

print('ESTOU PENSANDO EM UM NÚMERO ENTRE 0 E 5 [. . . ]')

sleep(3)

j = int(input('TENTE ADVINHAR: '))

if j == c:
    print('VOCÊ ACERTOU! PARABÉNS!!! ')
else: 
    print(f'QUE BOSTA, HEIN? PASSOU LONGE, EU PENSEI {c}')