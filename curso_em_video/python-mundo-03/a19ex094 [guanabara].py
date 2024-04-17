""" Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário em uma lista. No final mostre: 01 - Quantas pessoas foram 
cadastradas? / 02 - A média de idade do grupo / 03 - Uma lista com todas as mulheres / 04 - Uma lista com todas as pessoas com idade acima da média. """

galera = list()
pessoa = dict()

soma = media = 0 

while True: 
    pessoa.clear()
    pessoa['NOME'] = str(input('NOME: ')).strip().capitalize()
    while True:
        pessoa['SEXO'] = str(input('SEXO (M/F): ')).strip().capitalize()
        if pessoa['SEXO'] in 'MmFf':
            break
        print('ERRO! DIGITE APENAS "M" OU "F". ')
    pessoa['IDADE'] = int(input('IDADE: '))
    soma += pessoa['IDADE']
    galera.append(pessoa.copy())
    while True: 
        resp = str(input('CONTINUAR? (S/N): '))
        if resp in 'SsNn':
            break
        print('ERRO! RESPONDA APENAS "S" OU "N". ')
    if resp in 'Nn':
        break

print('=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade do grupo é {media}.')
print(f'C) As mulheres cadastradas foram ', end=' ')
for p in galera:
    if p['SEXO'] in 'Ff':
        print(f'{p["NOME"]}', end=' ')
print()
print(f'D) Lista de pessoas que estão acima da média de idade: ', end=' ')
for p in galera:
    if p['IDADE'] >= media:
        print('   ', end=' ')
        for k, v in p.items():
            print(f'{k}: {v}.', end=' ')
        print()
print(' <<<< ENCERRADO >>>> ')