""" Crie um módulo chamado moeda.py que tenha as funções incorporadas, aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esses módulos e use algumas 
dessas funções anteriores. """

import a22ex107moeda

p = float(input('DIGITE PREÇO: R$  '))

print(f'A metade de R$ {p} é R$ {a22ex107moeda.metade(p)}.')
print(f'O dobro de R$ {p} é R$ {a22ex107moeda.dobro(p)}.')
print(f'Aumentando em 10% temos R$ {a22ex107moeda.aumentar(p, 10)}.')