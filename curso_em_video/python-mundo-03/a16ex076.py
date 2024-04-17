""" Crie um programa que tenha uma tupla única com os nomes de produtos e seus preços na sequência. No final mostre uma listagem de preços organizando os dados 
de forma tabular. """

listagem = ('Lápis', 1.75,
            'Borracha', 2, 
            'Caderno', 15.90, 
            'Estojo', 25, 
            'Transferidor', 4.20, 
            'Compasso', 9.90,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print('\33[34m-\33[m' * 45)
print(f"\33[34mLISTAGEM DE PREÇOS\33[m".center(45))
print('\33[34m-\33[m' * 45)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<35}', end='')
    else:
        print(f' R${listagem[pos]:>7.2f}')