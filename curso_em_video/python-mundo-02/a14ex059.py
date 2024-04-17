""" Crie um programa que leia dois valores e mostre um menu na tela como o abaixo: 
Seu programa deverá realizar a operação solicitada pelo usuário em cada caso. 
1 - somar
2 - multiplicar
3 - maior
4 - novos números
5 - sair do programa """

from time import sleep

# QUEREMOS SABER DOIS VALORES ALEATÓRIOS INFORMADOS PELO USUÁRIO DO SISTEMA. 

n1 = int(input('VALOR 01: '))
n2 = int(input('VALOR 02: '))

# AGORA ESSE USUÁRIO TERÁ EM SUA FRENTE AS 5 OPÇÕES QUE PODERÁ REALIZAR COM O PROGRAMA. 

opcoes = 0
soma = 0
multiplicacao = 0 
maior = 0

opcoes = int(input('''AGORA NOS DIGA, O QUE FAZER COM ELES:
[ 1 ] SOMAR? 
[ 2 ] MULTIPLICAR? 
[ 3 ] QUAL MAIOR NÚMERO? 
[ 4 ] INSERIR 2 NOVOS NÚMEROS 
[ 5 ] SAIR DO PROGRAMA? 

DIGITE OPÇÃO: [     ]  '''))

while opcoes <= 4:
    if opcoes == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}. ')
        sleep(1)
        opcoes = int(input('''AGORA NOS DIGA, O QUE FAZER COM ELES:
[ 1 ] SOMAR? 
[ 2 ] MULTIPLICAR? 
[ 3 ] QUAL MAIOR NÚMERO? 
[ 4 ] INSERIR 2 NOVOS NÚMEROS 
[ 5 ] SAIR DO PROGRAMA? '''))
    if opcoes == 2:
        multiplicacao = n1 * n2
        print(f'{n1} X {n2} = {multiplicacao}. ')
        sleep(1)
        opcoes = int(input('''AGORA NOS DIGA, O QUE FAZER COM ELES:
[ 1 ] SOMAR? 
[ 2 ] MULTIPLICAR? 
[ 3 ] QUAL MAIOR NÚMERO? 
[ 4 ] INSERIR 2 NOVOS NÚMEROS 
[ 5 ] SAIR DO PROGRAMA? '''))
    if opcoes == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print(f'ENTRE {n1} E {n2}, O MAIOR VALOR É {maior}.')
        opcoes = int(input('''AGORA NOS DIGA, O QUE FAZER COM ELES:
[ 1 ] SOMAR? 
[ 2 ] MULTIPLICAR? 
[ 3 ] QUAL MAIOR NÚMERO? 
[ 4 ] INSERIR 2 NOVOS NÚMEROS 
[ 5 ] SAIR DO PROGRAMA? '''))
    if opcoes == 4:
        print('OK! VAMOS RECOMEÇAR COM NOVOS VALORES ENTÃO. ')
        n1 = int(input('VALOR 01: '))
        n2 = int(input('VALOR 02: '))
        opcoes = int(input('''AGORA NOS DIGA, O QUE FAZER COM ELES:
[ 1 ] SOMAR? 
[ 2 ] MULTIPLICAR? 
[ 3 ] QUAL MAIOR NÚMERO? 
[ 4 ] INSERIR 2 NOVOS NÚMEROS 
[ 5 ] SAIR DO PROGRAMA? 

DIGITE OPÇÃO: [     ]  '''))
    if opcoes == 5:
        print('FINALIZANDO')
        sleep(2)
        print('OBRIGADO POR USAR NOSSA APLICAÇÃO. SESSÃO ENCERRADA.')