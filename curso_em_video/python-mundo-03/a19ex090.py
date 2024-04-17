""" Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.  """

# AQUI ESTAMOS ESTUDANDO JÁ DICIONÁRIOS, ENTÃO TUDO DEVERÁ SER FEITO AO MÁXIMO EM DICIONÁRIOS.

alunos = dict()

nome = str(input('Nome: ')).strip().capitalize()
alunos['NOME'] = f'{nome}'
media = float(input('Média: '))
alunos['MÉDIA'] = f'{media}'

if media <= 5:
    alunos['SITUAÇÃO'] = 'REPROVADO'
elif media > 5 and media < 7:
    alunos['SITUAÇÃO'] = 'RECUPERAÇÃO'
elif media >= 7 and media <= 9.9:
    alunos['SITUAÇÃO'] = 'APROVADO'
elif media == 10:
    alunos['SITUAÇÃO'] = 'APROVADO COM DISTINÇÃO'

print('\n' + '=' * 50)
for k, v in alunos.items():
    print(f'{k}: {v}.')