""" Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. """

catetoOposto = float(input('Informe comprimento do cateto oposto: '))
catetoAdjacente = float(input('Informe comprimento do cateto adjacente: '))

print(f'A hipotenusa do triângulo vai medir {((catetoOposto + catetoAdjacente) ** 2) ** (1/2)}')