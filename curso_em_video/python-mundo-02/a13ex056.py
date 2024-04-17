""" Desenvolva um programa que leia nome, idade e sexo de 4 pessoas.
No final do programa mostre: 
A média de idade do grupo
Qual o nome do homem mais velho
Quantas mulheres tem menos de 20 anos """

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0

for p in range(1,5):
    print('\n' + '=' * 10 + f' {p}ª PESSOA: ' + '=' * 10 + '\n')
    nome = str(input(f'DIGITE {p}º NOME: ')).strip().upper()
    idade = int(input(f'DIGITE {p}º IDADE: '))
    sexo = str(input(f'DIGITE {p}º SEXO "M" OU "F": ')).upper()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1

mediaIdade = somaIdade / 4

print(f'A média de idades é de {mediaIdade}.')
print(f'O homem mais velho tem {maiorIdadeHomem} e se chama {nomeVelho}.')
print(f'O total de mulheres com menos de 20 anos é de {totMulher20}.')