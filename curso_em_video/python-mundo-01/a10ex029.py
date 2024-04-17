""" Escreva um programa que leia uma velocidade de um carro.
Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
Seu programa deverá também calcular a multa, sendo considerado R$ 7.00 por cada km excedido. """

v = int(input('VELOCIDADE DO CARRO: '))

if v <= 80:
    print('PARABÉNS, QUE BOSTA COMPRAR UM CARRO PARA ANDAR IGUAL A UMA LESMA ASSIM. ')
else: 
    multa = int((v - 80) * 7)
    print(f'VACILOU, SE FUDEU! FEZ MERDA E AGORA, VOCÊ FOI MULTADO EM R$  {multa}')

