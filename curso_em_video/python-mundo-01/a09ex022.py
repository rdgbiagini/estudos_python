""" Crie um programa que leia o nome completo de uma pessoa e retorne: 
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao todo, sem considerar espaços
Quantas letras tem o primeiro nome """

nome = str(input('Digite seu nome completo: ')).strip()

print(f'O nome todo em maiúsculo, fica: {nome.upper()}')
print(f'O nome todo em minúsculo, fica: {nome.lower()}')
print(f'Ao todo seu nome tem {(len(nome) - nome.count(" "))} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras.')

separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')