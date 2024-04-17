""" Crie uma tupla com os 20 primeiros colocados do Brasileirão atualmente, na ordem de colocação, para depois então mostrar: 
Os 5 primeiros colocados / Os 4 últimos colocados da tabela / Uma lista com todos os times em ordem alfabética / Em que posição na tabela está a Chapecoense? """

# UTILIZAÇÃO DE TUPLA - FAZENDO A RELAÇÃO DE TIMES DO CAMPEONATO BRASILEIRO DE FUTEBOL

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 
         'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 
         'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 
         'Atlético-GO')

# TUPLA FEITA EM ORDEM DE POSIÇÃO NO CAMPEONATO, NÃO EM ORDEM ALFABÉTICA OU QUALQUER OUTRA FORMA. 

print('=-=' * 30)
print(f'Lista de times do Brasileirão: {times}')
print('=-=' * 30)

print(f'Os 5 primeiros times, são: {times[0:5]}.')
print(f"Os 4 últimos colocados são: {times[-4:]}")
print('=-=' * 30)
print(f'A lista em ordem alfabética é: {sorted(times)}')
print('=-=' * 30)
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição no campeonato. ')