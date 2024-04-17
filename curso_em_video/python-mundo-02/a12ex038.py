""" Escreva um programa que leia dois números inteiros e compare os números.
Deverá exibir uma mensagem informando qual o valor maior, qual o menor ou se são iguais. 
Coloque cores diferentes para cada informação apresentada. """

# UMA APLICAÇÃO QUE LEIA DOIS NÚMEROS INTEIROS. 

n1 = int(input('nº 01: '))
n2 = int(input('nº 02: '))

# A APLICAÇÃO DEVERÁ COMPARAR OS NÚMEROS E DIZER QUAL É O MAIOR, QUAL O MENOR OU SE SÃO IGUAIS. 

maior = n1
menor = n1
iguais = ()

if n2 > n1:
    maior = n2
    print(f'O maior número é {maior}, o menor é o {menor}.')
elif n2 < n1:
    menor = n2
    print(f'O maior número é {maior}, o menor é o {menor}.')
elif n1 == n2:
    iguais = n1
    print('Os números são iguais.')
else:
    print(f'O maior número é {maior}, o menor é o {menor}.')
