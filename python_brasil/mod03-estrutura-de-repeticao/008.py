""" Faça um programa que leia 5 números e informe a soma e a média dos números. """

maior = 0 
soma = 0 
quant = 0


for i in range(1, 6):
    n = int(input('DIGITE VALOR: '))
    soma += n
    quant += 1
    if i == 1:
        maior = n
    elif i > 1:
        if n > maior:
            maior = n


print(f'O maior número digitado foi: {maior}')
print(f'A soma entre eles é: {soma}.')
media = (soma) / quant
print(f'A média entre eles é: {media}.')