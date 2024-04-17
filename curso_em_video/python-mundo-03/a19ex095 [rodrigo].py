""" Aprimore o desafio da questão 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador. """

todosJogadores = list()

jog = dict()

contJogadores = 0
total = 0 
artilharia = 0 

while True:
    jog['NOME'] = str(input('NOME: ')).strip().capitalize()
    contJogadores += 1
    jog['PARTIDAS'] = int(input('PARTIDAS: '))

    for g in range(1, jog['PARTIDAS'] + 1):
        gol = int(input(f'{g} PARTIDA: '))
        artilharia += gol
        jog['ARTILHARIA'] = f'{artilharia}'
    todosJogadores.append(jog.copy())
    ctn = str(input('DESEJA CONTINUAR? (S/N): ')).strip().capitalize()
    if ctn in 'Nn':
        break

print(todosJogadores)