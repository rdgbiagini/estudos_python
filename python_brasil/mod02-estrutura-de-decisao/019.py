""" Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16"""

num = int(input('Digite qualquer valor, entre 1 e 999: '))

# PRIMEIRO SE CAPTA O VALOR COMO UM NÚMERO INTEIRO. DEPOIS SE DESCOBRE QUANTAS DEZENAS, UNIDADES E CENTENAS E MILHARES EXISTEM. 

# FAZER COMO NÚMERO E NÃO COMO STRING DEIXA MARGEM PARA FAZERMOS MAIS ANÁLISES E NÃO APENAS PARA QUANTO TEM QUATRO DÍGITOS COMPLETOS. 

u = num // 1 % 10 
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

# ISSO SIGNIFICA: NUMERO DIVIDIDO POR 1000, 100, 10 OU 1 E O RESTO DA DIVISÃO DESSE RESULTADO POR 10 É A QUANTIDADE DE UNIDADES, DEZENAS, CENTENAS E MILHARES.

print(F'Analisando o número [ \33[31m{num}\33[m ] ')

# AÍ, O QUE NÃO APARECER SERÁ ZERADO, ENTÃO SE MANDAR UM NÚMERO SEM CENTENAS OU MILHARES TAMBÉM DARÁ CERTO. 

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
