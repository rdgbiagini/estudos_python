""" Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete / A mensagem "Reprovado", se a média for menor do que sete / A mensagem "Aprovado com Distinção", 
caso a média for igual a dez. """

nota1 = float(input('Digite primeira nota: '))
nota2 = float(input('Digite segunda nota: '))

media = (nota1 + nota2) / 2

print(f'A média das notas foi {media}.')

if media == 10:
    print('Aluno APROVADO COM DESTINÇÃO.')
elif media <=7:
    print('Aluno REPROVADO.')
else:
    print('Aluno APROVADO. ')