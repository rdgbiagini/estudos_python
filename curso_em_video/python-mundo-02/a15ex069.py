""" Crie um programa que leia o nome, a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar ao usuário se ele quer ou não continuar a cadastrar mais pessoas.
No final mostre: Quantas pessoas tem mais de 18 anos / Quantos homens foram cadastrados / Quantas mulheres tem menos de 20 anos.  """ 

# CONTADORES E ÍNDICES QUE SERÃO USADOS. ATÉ UNS A MAIS. 

homem = 0
mulher = 0
homensMais18 = 0
mulheresMenos20 = 0

# SEQUÊNCIA "INFINITA" DE INCLUSÃO DE DADOS POR PARTE DO USUÁRIO.

while True:
    nome = str(input('NOME: ')).strip().capitalize()
    idade = int(input('IDADE: '))
    sexo = input('SEXO ["M" / "F"]: ').strip().upper()
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Mm' and idade >= 18:
        homensMais18 += 1
    if sexo in 'Ff':
        mulher += 1
    if sexo in 'Ff' and idade <= 20:
        mulheresMenos20 += 1
    cont = input('DESEJA CONTINUAR? ["S" / "N"]: ')
    if cont in 'Nn': 
        break

# ESSE "BREAK" DE CIMA ENCERRA O "WHILE TRUE" COM UMA CONDICIONAL PARA UMA QUESTÃO ONDE O CARA VAI PODER ALIMENTAR O SISTEMA ETERNAMENTE.

print(f'Foram cadastrados {homem} homens. ')
print(f'Foram cadastradas {mulher} mulheres. ')
print(f'Foram cadastrados {homensMais18} homens com mais de 18 anos. ')
print(f'Foram cadastradas {mulheresMenos20} mulheres com menos de 20 anos. ')