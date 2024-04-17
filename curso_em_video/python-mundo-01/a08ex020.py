""" O mesmo professor do exercício anterior quer agora escolher a ordem de apresentação por seus alunos na apresentação de seus trabalhos. 
Ajude o a organizar a ordem com os mesmos quatro alunos do exercício anterior. """

# IMPORTAÇÃO DE BIBLIOTECAS

from random import shuffle

# PRIMEIRA COISA MESMO É PEGAR OS NOMES DOS 4 ALUNOS E INCLUIR ESSES 4 CORNOS EM UMA LISTA. 

n1 = str(input('01º ALUNO: '))
n2 = str(input('02º ALUNO: '))
n3 = str(input('03º ALUNO: '))
n4 = str(input('04º ALUNO: '))

# AQUI SE COLOCAM OS NOMES TODOS EM UMA LISTA, FAZENDO COM QUE ASSIM TENHAMOS UM "BANCO DE DADOS" DE ALUNOS PARA PODERMOS FAZER ENTÃO O SORTEIO. 

lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação, será: {lista}')