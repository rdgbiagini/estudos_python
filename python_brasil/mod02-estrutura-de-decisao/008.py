""" Faça um programa que pergunte o preço de três produtos e informe: 
qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. """

prod1 = int(input('Informe preço do produto número 01: '))
prod2 = int(input('Informe preço do produto número 02: '))
prod3 = int(input('Informe preço do produto número 03: '))

menor = ()

if prod1 < prod2 and prod1 < prod3:
    menor = prod1
elif prod2 < prod1 and prod2 < prod3:
    menor = prod2
else:
    menor = prod3

print(f'O melhor produto a ser comprado é o {menor}, pois é o mais barato.')