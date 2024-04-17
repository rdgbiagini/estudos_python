""" Faça um programa que leia algo pelo teclado. 
E mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela. """

a = input('Digite algo: ')

# ANÁLISES DA STRING

tipo = type(a)
espaco = a.isspace()
numero = a.isnumeric()
alfa = a.isalpha()
alfanum = a.isalnum()
maiusc = a.isupper()
minusc = a.islower()
capitalizada = a.istitle()

# RESULTADOS

print(f'O tipo da informação inserida é {tipo}.')
print(f'Só tem espaços? {espaco}')
print(f'É um número? {numero}')
print(f'É alfabético? {alfa}')
print(f'É alfanumérico? {alfanum}')
print(f'É maiúscula? {maiusc}')
print(f'É minúscula? {minusc}')
print(f'Está capitalizada? {capitalizada}')