""" Melhore o jogo do desafio 028, onde a computação vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para acertar e vencer. """

""" EXERCÍCIO 058:

Escreva um programa que faça o computador pensar em um número de 0 a 5 e peça para o jogador tentar adivinhar o número pensado. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

c = randint(0, 5)

print('ESTOU PENSANDO EM UM NÚMERO ENTRE 0 E 5 [. . . ]')

sleep(3)

j = int(input('TENTE ADVINHAR: '))

if j == c:
    print('VOCÊ ACERTOU! PARABÉNS!!! ')
else: 
    print(f'QUE BOSTA, HEIN? PASSOU LONGE, EU PENSEI {c}') """

# PRIMEIRO PASSO É CRIAR O COMPUTADOR E COMO ELE VAI SORTEAR UM NÚMERO. ENTÃO VAMOS USAR A BIBLIOTECA RANDOM.

# BIBLIOTECA

from random import randint

# DADOS INSERIDOS

computador = randint(0, 10)
acertou = False
palpites = 0
print(computador)

while not acertou:
    jogador = int(input('SEU PALPITE: [   ] '))
    palpites += 1
    if jogador == computador:
        print(f'ACERTOU, MISERÁVI! QUEM TE ENSINOU? SÓ PRECISOU DE {palpites} TENTATIVAS ESSE ANIMAL. ')
    else:
        if jogador < computador:
            print('Mais... Tente de novo. ')
        elif jogador > computador:
            print('Menos.... Tente de novo. ')
