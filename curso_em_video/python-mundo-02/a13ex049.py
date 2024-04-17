""" Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço "for". """

""" RESOLUÇÃO ANTIGA DO EXERCÍCIO 009:

n = int(input('De qual número você quer ver a taboada? '))

print('=' * 30)
print('\n')
print(f'A TABOADA DO {n} É:')
print('\n')
print(f'{n} x 01 = {n*1}')
print(f'{n} x 02 = {n*2}')
print(f'{n} x 03 = {n*3}')
print(f'{n} x 04 = {n*4}')
print(f'{n} x 05 = {n*5}')
print(f'{n} x 06 = {n*6}')
print(f'{n} x 07 = {n*7}')
print(f'{n} x 08 = {n*8}')
print(f'{n} x 09 = {n*9}')
print(f'{n} x 10 = {n*10}')
print('\n')
print('=' * 30) """

print('=' * 16)
print('TABOADA!')
print('=' * 16)
print('\n')

numero = int(input('DIGITE UM VALOR PARA VER A SUA TABOADA ENTRE 1x E 10x: \33[34m[   ]:\33[m '))
print('\n')

for c in range(1, 11):
    print(f'{numero} x {c} = {numero * c}')