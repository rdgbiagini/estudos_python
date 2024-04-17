""" Faça um programa que calcule o mostre a média aritmética de N notas. """

contNota = 1 
somaNota = 0 
mediaNota = 0 

while True:
    n = int(input(f'{contNota}ª nota: (Digite 999 para sair):  '))
    if n == 999:
        break
    else: 
        contNota += 1
        somaNota += n
        mediaNota = somaNota / contNota - 1
        print(f'Foram inseridas {contNota} notas e sua média foi {mediaNota}.')
