""" Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina. Ex:  Nota 1: 4.5 Nota 2: 8.5 A média entre 4.5 e 8.5 é igual a 6.5 """

n1 = float(input('nota 01: '))
n2 = float(input('nota 02: '))

media = (n1 + n2) / 2

print(f'Nota 1: {n1} Nota 2: {n2}. A média entre {n1} e {n2} é igual a {media}.')