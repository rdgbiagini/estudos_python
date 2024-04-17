""" Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de um a vinte. 
Seu programa deverá ler o número pelo teclado entre 0 e 20 (em numeral) e na sequência mostrar ele escrito por extenso. Só deve aceitar números entre 0 e 20.
Depois, durante a aula o Guanabara pediu para evoluir o programa, para fazer que ele mantenha esse loop. 
Essa foi a situação que fez meter esse break e depois "else: n" puro. """

# ESTAMOS AQUI USANDO UMA TUPLA, ONDE, MESMO SEM AS ASPAS TRIPLAS O VS CODE ENTENDEU A FORMATAÇÃO. PORÉM TEM QUE DEIXAR OS PARÊNTESES ENTRE ELES. 
# AS TUPLAS POR ESSÊNCIA EXISTEM E FUNCIONAM MESMO QUE SEM OS PARÊNTESES
# PORÉM NESSE CASO ESTAMOS PRECISANDO DE UMA FORMATAÇÃO MAIS ESPECÍFICA PARA TENTAR FAZER TUDO EM UMA TELA 

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# CONDIÇÃO "WHILE TRUE" QUE GERA A REPETIÇÃO NO CÓDIGO ATÉ QUE A CONDIÇÃO DO IF SEJA APRESENTADA PARA QUE SEJA FEITO O "BREAK".
# NESSE CASO SE NÃO FOR ISSO, REPETE O CÓDIGO "N" APENAS. PODERIA SE COLOCAR VÁRIAS SITUAÇÕES? ACREDITO QUE NÃO GERARIA PROBLEMAS. 

while True:
    n = int(input('''DIGITE NÚMERO ENTRE 0 E 20: [   ] '''))
    if 0 <= n <= 20:
        print(f'Você digitou o número {cont[n].upper()}. ')
        segue = str(input('DESEJA CONTINUAR? ["S" / "N" ]'))
        if segue in 'Nn':
            print('Obrigado. Volte sempre.')
            break
        else:
            n