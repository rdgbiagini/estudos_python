""" Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que: Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial; A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário. """

def aumentoSalarial():
    salario = 1000
    taxa = 0.015
    aumento = salario + (salario * taxa)
    variacao = salario * taxa

    for a in range(1996, 2024):
        print(f'No ano de {a} o salário do empregado foi de R$ {salario} para variação de R$ {variacao}, com uma taxa de {taxa} e total final de {aumento}.')
        taxa = (taxa * 2)
        salario = salario + variacao

aumentoSalarial()
