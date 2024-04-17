""" Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o usuário digitar um número negativo. """

while True:
    tab = int(input('QUAL TABOADA VOCÊ QUER VER? '))
    if tab <=0:
        break
    for c in range(1,11):
        print(f'{tab} x {c} = {tab * c}')

print('TABOADA ENCERRADA. VOLTE SEMPRE.')
