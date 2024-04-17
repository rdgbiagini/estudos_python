""" Crie um programa que leia vários números e coloque-os em uma lista. Depois disso, nos mostre: 01 - Quantos números foram digitados? / 02 - A lista de valores ordenada de forma 
decrescente / 03 - Se o valor 5 foi digitado e se ele está ou não na lista.  """

# CAPTAÇÃO DE VALORES POR PARTE DO USUÁRIO. 

valores = []

while True:
    valores.append(int(input('VALOR: ')))
    resp = str(input('CONTINUAR? [ S / N ]? '))
    if resp in 'Nn':
        break

print('=' * 30)

print(f'VOCÊ DIGITOU {len(valores)} VALORES. ')

# PRIMEIRO A GENTE VAI JOGAR O COMANDO ".SORT()" AQUI FORA, PARA QUE ELE FAÇA COM ESSE REVERSE A LISTA DE FORMA DECRESCENTE. 
# DEPOIS DISSO SE USA NO PRINT FORMATADO O VALOR PARA "valores" NORMALMENTE MESMO, SEM PRECISAR COLOCAR O REVERSE=TRUE DENTRO DO FORMATADO. 

valores.sort()
print(f'A LISTA CRESCENTE É: {valores}')

valores.sort(reverse=True)
print(f'A LISTA DECRESCENTE É: {valores} ')

if 5 in valores:
    print('O VALOR 5 FAZ PARTE DA LISTA. ')
else:
    print('O VALOR 5 NÃO FOI ENCONTRADO NA LISTA. ')

print('=' * 30)

