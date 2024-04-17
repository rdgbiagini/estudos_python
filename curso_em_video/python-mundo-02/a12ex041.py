""" A confederação nacional de natação precisa de um programa que leia a idade de um atleta e identifique a sua categoria de forma automática.
Até 9 anos mirim
9 a 14 é infantil
15 a 19 é juniores
20 anos é senior
acima de 20 anos é master """

idade = int(input('IDADE DO ATLETA: '))

if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIORES')
elif idade > 19 and idade <= 20:
    print('SENIOR')
else:
    print('MASTER')
