""" Faça um jogo de par ou ímpar. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. """

from random import randint

while True:
    jogador = int(input('DIGITE VALOR: '))
    computador = randint(0, 11)
    total = computador + jogador
    tipo = ' '
    vitoria = 0

    while tipo not in 'PI':
        tipo = str(input('PAR OU ÍMPAR? [ "P" / "I" ]: ')).strip().upper()
    print(f'Você jogou {jogador} e o computador jogou {computador}. A soma é {total}.')

    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU.')
            vitoria += 1
        else: 
            print('VOCÊ PERDEU.')
            break
    if tipo == 'I':
        if total % 2 != 0:
            print('VOCÊ PERDEU.')
        else:
            break

