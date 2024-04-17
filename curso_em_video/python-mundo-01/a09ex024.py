""" Crie um programa que leia o nome da cidade de uma pessoa e diga se ela começa ou não com o nome "SANTO" """

cid = str(input('Em qual cidade você nasceu? ')).strip().upper()
print(cid[:5] == 'SANTO')