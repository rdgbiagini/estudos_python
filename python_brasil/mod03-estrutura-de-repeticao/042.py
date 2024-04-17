""" Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo. """

cont0a25 = 0 
cont26a50 = 0 
cont51a75 = 0 
cont76a100 = 0

while True: 

    num = int(input('Digite valor inteiro e positivo: (entre 0 e 100 - digite valor negativo para encerrar a aplicação): '))
    if num < 0:
        break

    if num >= 0 and num < 26:
        cont0a25 += 1
    elif num >= 26 and num < 51:
        cont26a50 += 1
    elif num >= 51 and num < 76:
        cont51a75 += 1
    elif num >= 76 and num <= 100:
        cont76a100 += 1

print(f'Tivemos {cont0a25} numeros no intervalor de [0 - 25]')
print(f'Tivemos {cont26a50} numeros no intervalor de [26 - 50]')
print(f'Tivemos {cont51a75} numeros no intervalor de [51 - 75]')
print(f'Tivemos {cont76a100} numeros no intervalor de [76 - 100]')