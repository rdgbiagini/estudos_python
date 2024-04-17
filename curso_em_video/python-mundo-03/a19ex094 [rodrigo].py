""" Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário em uma lista. No final mostre: 01 - Quantas pessoas foram 
cadastradas? / 02 - A média de idade do grupo / 03 - Uma lista com todas as mulheres / 04 - Uma lista com todas as pessoas com idade acima da média. """

todos = list() # LISTA PRINCIPAL COM TODOS. RECEBE TODOS OS DICIONÁRIOS. QUANTOS O USUÁRIO QUISER. 
todasMulheres = list() # LISTA SÓ COM OS DADOS DE MULHERES INCLUÍDAS NA BIBLIOTECA. 
acimaMedia = list() # FALTA FAZER ESSE. #PESSOAS COM IDADE ACIMA DA MÉDIA. 

bDados = dict() # DICIONÁRIO TEMPORÁRIO ONDE TODOS OS DADOS INSERIDOS PELO USUÁRIO SERÁ GUARDADO. 

contPessoas = 0 # CONTADOR DE PESSOAS
somaIdade = 0 # SOMA DA IDADE DE TODOS PARA FAZER A MÉDIA. 

contErrosSexo = 0 

while True:
    bDados['NOME'] = str(input('NOME: ')).strip().capitalize()
    contPessoas += 1
    bDados['SEXO'] = str(input('SEXO (M/F): ')).strip()
    while bDados['SEXO'] not in 'MmFf':
        print('VALOR INVÁLIDO. RESPONDA APENAS "M" OU "F", POR FAVOR.')
        bDados['SEXO'] = str(input('SEXO (M/F): ')).strip()
        contErrosSexo += 1
    if bDados['SEXO'] in 'Ff':
        todasMulheres.append(bDados.copy())
    bDados['IDADE'] = int(input('IDADE: '))
    somaIdade += bDados['IDADE']
    mediaIdade = (somaIdade) / contPessoas
    todos.append(bDados.copy())
    bDados.clear()
    segue = str(input('CONTINUAR INSERINDO PESSOAS? (S/N): ')).strip().capitalize()
    if segue in 'Nn':
        break

print('=' * 200 + '\n' + f'O dicionário que deverá estar vazio é? {bDados}.')
print('=' * 200 + '\n' + f'A lista que tem todo mundo que foi inserido pelo usuário é: {todos}.')
print('=' * 200 + '\n' + f'A quantidade de pessoas incluídas é: {contPessoas}.')
print('=' * 200 + '\n' + f'A soma das idades do grupo é: {somaIdade}.')
print('=' * 200 + '\n' + f'A média de idade do grupo é: {mediaIdade}.')
print('=' * 200 + '\n' + f'A lista só com as mulheres é: {todasMulheres}.')
print('=' * 200 + '\n' + f'A lista de pessoas acima da média de idade do grupo é: {acimaMedia}.')
print('=' * 200 + '\n' + f'A pessoa errou a digitação do sexo {contErrosSexo} vezes')
