""" Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.  """

def area(largura, comprimento):
    area = largura * comprimento
    print(f'Para comprimento de {comprimento} e largura de {largura}, temos um terreno com uma áream de {area} m². ')

l = float(input('LARGURA DO TERRENO: '))
c = float(input('COMPRIMENTO DO TERRENO: '))
area(l, c)