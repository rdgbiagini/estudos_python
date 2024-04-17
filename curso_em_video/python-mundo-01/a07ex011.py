""" Faça um programa que leia a altura e a largura de uma parede em metros e calcule sua área. 
Daí dê a quantidade de tintas necessárias para pintar toda essa parede.
Considere que cada litro de tinta pinta 2m² de parede. """

h = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))

area = h * l

print(f'Uma vez que é uma parede com {h}m de altura e com {l}m de largura, temos {h * l}m de area total.')
print(f'Considerando esses dados e que cada litro de tinta pinta 2m² precisamos de {(h * l) / 2} litros de tinta.')
