""" Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar de ler quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram inseridos e qual foi a soma entre eles. (desconsiderando a flag de parada) """

valor = int(input('DIGITE VALOR: '))

cont = 0
soma = 0

while valor != 999:
    cont += 1
    soma += valor
    valor = int(input('DIGITE VALOR: '))

print(f'Foram inseridos {cont} e a soma entre eles é {soma}.')