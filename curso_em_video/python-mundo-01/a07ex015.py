""" Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa 60 / dia e 0.15 / quilômetro rodado. """

km = float(input('Quantos km foram rodados com o carro? '))
dias = int(input('Quantos dias ficou alugado? '))

precoDias = int(dias * 60)
precoKm = int(km * 0.15)
precoTotal = precoDias + precoKm

print(f'O carro foi alugado por {dias} dias, a um custo de R$ 60.00 / dia e rodou {km} a um custo de R$ 0.15 / quilômetro percorrido. ' )
print(f'Portanto deve {precoDias} pelos dias e {precoKm} pelos km rodados, com um total de {precoTotal}. ')