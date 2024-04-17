""" Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols 
feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. """

jog = dict()
total = 0 
artilharia = 0 

jog['NOME'] = str(input('NOME: ')).strip().capitalize()
jog['PARTIDAS'] = int(input('PARTIDAS: '))

for g in range(1, jog['PARTIDAS'] + 1):
    gol = int(input(f'{g} PARTIDA: '))
    artilharia += gol
    jog['ARTILHARIA'] = f'{artilharia}'

print(jog)