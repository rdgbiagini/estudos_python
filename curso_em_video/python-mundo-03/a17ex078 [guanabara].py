""" lanche = ['hamburguer', 'sorvete', 'pudim', 'picole']

print(lanche)

lanche[2] = 'casquinha'

print(lanche) """

""" valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor: {v}.')
print(f'Cheguei ao final. ') """

""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor digitado e os respectivos valores de suas posições. """

# LISTA QUE DEVE SER INCLUÍDOS OS VALORES APRESENTADOS PELO USUÁRIO, NA ORDEM DADA POR ELE. 

listaNum = []

# CÁLCULO DE MAIOR E MENOR. 

maior = 0
menor = 0 

for c in range(0, 8):
    listaNum.append(int(input(f'DIGITE {c + 1}º NÚMERO: ')))
    
    if c == 0:
        maior = menor = listaNum[c]
    else: 
        if listaNum[c] > maior:
            maior = listaNum[c]
        if listaNum[c] < menor:
            menor = listaNum[c]

print(f"A lista que você digitou foi: {listaNum}.")

print(f'O maior valor digitado foi {maior}, que apareceu na(s) posição(ções): ', end=' ')

for i, v in enumerate(listaNum):
    if v == maior:
        print(f'{i}... ', end=' ')
    print()

print(f'O menor valor digitado foi {menor}, que aparece na(s)  posição(ções): ', end=' ')

for i, v in enumerate(listaNum):
    if v == menor:
        print(f'{i}...', end=' ')
    print()
