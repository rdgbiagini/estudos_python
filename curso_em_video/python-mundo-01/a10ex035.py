""" Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não fazer um triângulo. 
Regra: A soma de dois lados é sempre menor do que a do terceiro lado. """

titulo = 'ANALISADOR DE TRIÂNGULOS'

# PRATICANDO COLOCAR CORES NAS COISAS DOS CÓDIGOS.

print('\n' + '\33[7m=\33[m' * (len(titulo) * 2)) # COR "NEGATIVA" PARA COLOCAR FUNDO BRANCO E LETRA PRETA

print('\33[0;30;41m{:^50}\33[m'.format (titulo)) # COR PARA COLOCAR FUNDO VERMELHO E LETRA BRANCA

print('\33[7m=\33[m' * (len(titulo) * 2) + '\n') # COR NEGATIVA DE NOVO

r1 = int(input('\33[33mRETA 01\33[m: '))
r2 = int(input('\33[34mRETA 02\33[m: '))
r3 = int(input('\33[35mRETA 03\33[m: '))

if r1 < r2 + r3 and r2 < r3 + r2 and r3 + r2 + r1:
    print('SIM, PODEMOS FAZER UM TRIÂNGULO. ')
else:
    print('FODA-SE A CARALHA DO TRIÂNGULO. ')