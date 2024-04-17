""" Desenvolva um programa que pergunte a distância de uma viagem em km. 
Calcule o preço da passagem cobrando: 
R$ 0.50 por km para viagens até 200km de distância
R$ 0.45 para viagens acima de 200km de distância """

d = float(input('DISTÂNCIA A SER PERCORRIDA: '))
preco = 0

if d <= 200:
    preco = d * 0.50
else:
    preco = d * 0.45

print(f'VOCÊ ENTÃO VAI PAGAR R$ {preco}')