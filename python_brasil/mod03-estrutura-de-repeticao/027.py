""" Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos. """

# ==================================================================================================================================================================================== #
# BIBLIOTECAS, VARIÁVEIS GLOBAIS, CONTADORES E DEMAIS INFORMAÇÕES PERTINENTES. 
# ==================================================================================================================================================================================== #

somaAlunos = 0 

# ==================================================================================================================================================================================== #
# PRIMEIRO QUERO SABER QUANTAS TURMAS, PORQUE ISSO VAI GERAR O LAÇO FOR NECESSÁRIO. 
# ==================================================================================================================================================================================== #

qTurmas = int(input('Quantidade de turmas: '))

for t in range(1, qTurmas + 1):

    qAlunos = int(input(f'Na {t}ª Turma, temos quantos alunos? '))
    somaAlunos += qAlunos

mediaAlunos = somaAlunos / qTurmas

print(f'Temos um total de {qTurmas} turmas, com uma média de {mediaAlunos} alunos por turma.')