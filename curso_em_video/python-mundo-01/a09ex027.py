""" Faça um programa que leia o nome completo de uma pessoa e mostre em seguida apenas o primeiro e o último nome separadamente. """

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(nome)
print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu último nome é: {nome[len(nome) - 1]}')