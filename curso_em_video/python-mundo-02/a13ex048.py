""" Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo entre 1 e 500. """

cont = 0
soma = 0

for c in range(1,501):
    if c % 2 != 0 and c % 3 == 0: 
        print(c, end=' ')
        cont += 1
        soma += c
print(f'\nA soma dos \33[33m{cont}\33[m números ímpares e múltiplos de 3 é de \33[35m{soma}\33[m.')