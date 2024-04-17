""" Escreva um programa que leia um valor em metros e exiba ele convertido em: 
centímetros e milímetros. """

m = float(input('Digite uma medida em metros: '))

print(f'Essa medida de {m}m equivale a: ')
print(f'{m * 10} cm')
print(f'{m * 100} mm')