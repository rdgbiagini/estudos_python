""" Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade, considerando: 
Menos de 18 anos ele ainda vai se alistar no exército
Se ele tem 18 anos já é hora de se alistar. 
Se ele já passou dos 18 tem que informar que já passou do tempo para ele se alistar e poder correr para compensar o atraso.
Colocar cores diferentes. """

# BIBLIOTECAS A SEREM IMPORTADAS

from datetime import date

# INFORMAÇÕES A SEREM COLETADAS OU INSERIDAS PELO USUÁRIO.

ano = int(input('Qual seu ano de nascimento? '))
hoje = date.today().year
idade = hoje - ano
atraso = idade - 18

if idade < 18:
    print('Tranquilo. Você ainda não está na idade de se alistar ao exército. Aproveite para ser feliz.')
elif idade == 18:
    print('SE FUDEU! ESTÁ NA IDADE DE SE ALISTAR AO EXÉRCITO. VAI SE FUDER.')
else:
    print(f'Se não se alistou ainda, já está com {atraso} anos de atraso. ')

