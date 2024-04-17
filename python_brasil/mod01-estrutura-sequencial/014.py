""" João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes > o estabelecido pelo regulamento de São Paulo (50 quilos), paga uma multa de R$ 4,00 / quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas. """

peso = float(input('Informe quantos Kgs trouxe: [   ]'))

excesso = peso - 50

if excesso >= 0:
    print(f'Deve ser pago R$ {excesso * 4}')
else: 
    print('Não há multa a ser paga.')