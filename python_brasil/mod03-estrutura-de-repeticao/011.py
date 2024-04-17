""" Altere o programa anterior para mostrar no final a soma dos números. """

""" EXERCÍCIO 010 --> Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input('DIGITE INÍCIO DO INTERVALO: '))
n2 = int(input('DIGITE FINAL DO INTERVALO: '))

for i in range(n1, n2):
    print(i) """

n1 = int(input('Início do intervalo: '))
n2 = int(input('Final do intervalo (inclusive): '))
soma = 0 

for i in range(n1, n2 + 1):
    soma += i
    print(i)

print(f'A soma foi {soma}')