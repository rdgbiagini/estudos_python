""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final mostre um boletim contendo a média de cada um e permita que o usuário possa 
mostrar as notas de cada aluno individualmente.  """

ficha = list()

while True:
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA 01: '))
    nota2 = float(input('NOTA 02: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('QUER CONTINUAR? [S/N]: '))
    if resp in 'Nn':
        break

print(f'=' * 30)
print(f'{"Nº":<10}{"NOME":^10}{"MÉDIA":^10}')
print(f'=' * 30)

for i, a in enumerate(ficha):
    print(f'{i:^5}{a[0]:^10}{a[2]:^8.1f}')
while True:
    print('=' * 30)
    opc = (int(input('MOSTRAR NOTAS DE QUAL ALUNO? ')))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'NOTAS DE {ficha[opc][0]} são {ficha[opc][1]}')
print('VOLTE SEMPRE.')