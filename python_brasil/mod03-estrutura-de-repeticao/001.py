""" Faça um programa que peça uma nota entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. """

while True: 
    numero = int(input('informe valor entre 0 e 10. [   ]: '))
    if numero <= 0:
        print('NÚMERO INVÁLIDO. TENTE NOVAMENTE. ')
        numero
    elif numero >= 11: 
        print('NÚMERO INVÁLIDO. TENTE NOVAMENTE. ')
        numero
    else:
        print(f'NÚMERO VÁLIDO. O VALOR DIGITADO FOI {numero}.')
        break