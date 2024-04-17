""" Faça um programa que leia nome e peso de várias pessoas, guardando tudo em listas individuais, dentro de uma lista grande, no final mostre: 01 - Quantas pessoas foram cadastradas / 
02 - Uma listagem com as pessoas mais pesadas / 03 - Uma listagem com as pessoas mais leves.  """

geral = []
temp = []
contPessoa = 0
maior = 0
menor = 0

while True: # PORQUE ELE FALA QUE QUER "VÁRIAS PESSOAS", OU SEJA, SEM DEFINIÇÃO, OU ATÉ O USUÁRIO ENCERRAR
    contPessoa += 1
    print('\33[33m=\33[m' * 30)
    print(f'DADOS DA {contPessoa}ª PESSOA:')
    print('\33[33m=\33[m' * 30)
    nome = str(input('NOME: '))
    if len(geral) == 0:
        maior = temp[1]
        menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]


    temp.append(nome)
    peso = float(input('PESO: '))
    temp.append(peso)
    geral.append(temp[:])   
    temp.clear()
    prx = str(input('CONTINUAR? [S/N] '))
    if prx in 'Nn':
        break

print(f'A) FORAM INSERIDAS {len(geral)} PESSOAS. ')
geral.sort()

if len(geral) > 1:
    geral.sort()
    print(f'A mais pesada é {maior} e a mais leve {menor}.')

# RESULTADOS DA QUESTÃO:

