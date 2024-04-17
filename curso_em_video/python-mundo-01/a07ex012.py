""" Faça um programa que leia o preço de um produto e mostre seu novo preço com desconto de 5%. """

prod = float(input('Qual o valor do produto? '))

print(f'O valor do produto é {prod} e seu desconto é 5%, então seu valor final é {prod * 0.95}')
print(f'Se pagar parcelado terá um acréscimo de 10% portanto o valor final será {prod * 1.10}')
print(f'Se pagar à vista e em dinheiro terá ainda um desconto de + 5% então o valor final será de {prod * 0.90}')
