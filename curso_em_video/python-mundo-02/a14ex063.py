""" Escreva um programa que leia um número n inteiro qualquer e mostre na sua tela os números n primeiros elementos de uma sequência fibonacci.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8 """

n = int(input('DIGITE QUANTIDADE: '))

t1 = 0 
t2 = 1

cont = 3

while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3 
    cont += 1
print('FIM! ')