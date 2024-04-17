""" Refaça o desafio 35 dos triângulos incluindo agora a informação se o triângulo que ali se forma é equilátero, isóceles ou escaledo. 
Equilátero tem todos os lados iguais.
Isósceles tem dois lados iguais.
Escaleno tem todos os lados diferentes. """

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
    if r1 == r2 == r3:
        print('E é um triângulo equilátero. Onde todos os lados são iguais.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('E é um triângulo Isósceles. Onde tem dois lados iguais.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('E é um triângulo Escaleno. Onde todos os lados são diferentes.')
else:
    print('FODA-SE A CARALHA DO TRIÂNGULO. ')