""" Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta da inserção sem usar o "sort()". 
No final, mostre a lista ordenada na tela. """

lista = []

for c in range(0, 5):
    n = int(input('VALOR: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0 
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('=' * 30)
print(f'Os valores digitados na ordem, foram: {lista}.')
print(f'=' * 30)