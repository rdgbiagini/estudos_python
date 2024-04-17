""" Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo os nomes deles e escrevendo o nome escolhido. """

# IMPORTAÇÃO DE BIBLIOTECAS

from random import choice

# PRIMEIRA COISA MESMO É PEGAR OS NOMES DOS 4 ALUNOS E INCLUIR ESSES 4 CORNOS EM UMA LISTA. 

n1 = str(input('Digite nome do primeiro aluno: '))
n2 = str(input('Digite nome do segundo aluno: '))
n3 = str(input('Digite nome do terceiro aluno: '))
n4 = str(input('Digite nome do quarto aluno: '))

# AQUI SE COLOCAM OS NOMES TODOS EM UMA LISTA, FAZENDO COM QUE ASSIM TENHAMOS UM "BANCO DE DADOS" DE ALUNOS PARA PODERMOS FAZER ENTÃO O SORTEIO. 

lista = [n1, n2, n3, n4]
escolhido = choice(lista) # ESSA FUNÇÃO CHOICE QUEM FAZ O SORTEIO DOS ALUNOS

print(f'O aluno escolhido foi: {escolhido}')