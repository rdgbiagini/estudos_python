""" Adapte o código do Desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado. """

import a22ex108moeda

p = float(input('DIGITE PREÇO: R$  '))

print(f'A metade de {a22ex108moeda.moeda(p)} é {a22ex108moeda.moeda(a22ex108moeda.metade(p))}.')
print(f'O dobro de {a22ex108moeda.moeda(p)} é {a22ex108moeda.moeda(a22ex108moeda.dobro(p))}.')
print(f'Aumentando em 10% temos {a22ex108moeda.moeda(a22ex108moeda.aumentar(p, 10))}.')