""" Faça um programa que tenha uma função chamada ficha(), que recebe dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.  """

def ficha(jog='<desconhecido>', gols=0):
    print(f'O jogador {jog} fez {gols} gols no campeonato.')

# PROGRAMA PRINCIPAL:

n = str(input('NOME: '))
g = str(input('GOLS: '))
if g.isnumeric():
    g.strip()
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)