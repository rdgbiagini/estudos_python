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

for n in range(0, 5):
    listaNum.append(int(input(f'DIGITE {n}º NÚMERO: ')))

# NESSE CASO A MINHA SOLUÇÃO É PERFEITAMENTE APLICÁVEL PORQUE NÃO SE TEM MUITAS VARIÁVEIS DE ERRO, MAS SE FOSSE UM SISTEMA MAIS SOLTO, A DO GUANABARA É MAIS "ANTI BURRO"

print(f"A lista que você digitou foi: {listaNum}. ")
listaNum.sort()
print(f'O maior valor digitado foi o {listaNum[-1]}. ')