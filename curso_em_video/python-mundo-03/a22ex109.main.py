""" Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda()
desenvolvida no desafio 108. """

import a22ex109moeda

p = float(input('DIGITE PREÇO: R$  '))

print(f'A metade de {a22ex109moeda.moeda(p)} é {a22ex109moeda.metade(p, True)}.')
print(f'O dobro de {a22ex109moeda.moeda(p)} é {a22ex109moeda.dobro(p, True)}.')
print(f'Aumentando em 10% temos {a22ex109moeda.aumentar(p, 10)}.')
print(f'Diminuindo 13% temos {a22ex109moeda.diminuir(p, 13)}.')