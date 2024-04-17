""" Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente, até ter um valor correto. """

sexo = input('SEXO: [DIGITE APENAS: "M" OU "F"]: ').strip().upper()[0]

while sexo not in 'MmFf':
    sexo = input(f'CARALHO! NÃO SABE LER ESSA PORRA NÃO? TENTE DE NOVO, CARALHO [   ]. ').strip().upper()[0]

print(f'Parabéns! Você respondeu corretamente. O sexo digitado foi {sexo}')