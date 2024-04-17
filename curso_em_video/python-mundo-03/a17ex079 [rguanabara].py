""" Crie um programa em que o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final serão exibidos todos os valores únicos dessa lista, em ordem crescente.  """

numeros = list()

while True: 
    n = int(input('DIGITE NÚMERO: '))
    if n not in numeros:
        numeros.append(n)
        print('VALOR ADICIONADO COM SUCESSO.')
    else:
        print('VALOR DUPLICADO. NÃO SERÁ ADICIONADO. ')
    r = str(input('QUER CONTINUAR? '))
    if r in 'Nn':
        break

print('=' * 30)
print(numeros.sort())
print('=' * 30)