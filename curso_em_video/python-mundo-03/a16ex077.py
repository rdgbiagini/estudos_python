""" Crie um programa que tenha uma tupla com várias palavras aleatórias, mas sem acentuação gráfica. Mostre, para cada palavra, quais são as suas vogais.  """

palavras = ('casa', 'sapato', 'mesa', 'jantar', 'cadeira', 'janela',
             'armario', 'experiencia', 'viagem')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')