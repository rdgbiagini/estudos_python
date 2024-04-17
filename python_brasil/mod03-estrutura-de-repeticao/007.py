""" Faça um programa que leia 5 números e informe o maior número. """

maior = 0 

for i in range(1, 6):
    n = int(input('DIGITE VALOR: '))
    
    if i == 1:
        maior = n
    elif i > 1:
        if n > maior:
            maior = n


print(f'O maior número digitado foi: {maior}')
    