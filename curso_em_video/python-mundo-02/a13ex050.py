""" Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado por ímpar, desconsidere-o. """

# CRIANDO AQUI PRIMEIRO UM CONTADOR E UM SOMADOR PARA PODER ACUMULAR AS INFORMAÇÕES QUE SERÃO DADAS PELO USUÁRIO.

soma = 0
cont = 0

# O LAÇO "FOR" AQUI É PARA VOCÊ NÃO PRECISAR FICAR FAZENDO "DIGITE UM VALOR" TODA VEZ E ELE SER CAPAZ DE ACUMULAR AS INFORMAÇÕES.

for c in range(1,7):
    n = int(input(f'Digite o {c}º valor: ')) # O INPUT PODE SER EDITADO PARA VOCÊ TER UMA VISUALIZAÇÃO DINÃMICA.
    if n % 2 == 0: 
        soma += n
        cont += 1
print(f'Você informou {cont} números PARES e a soma entre eles é {soma}.')
