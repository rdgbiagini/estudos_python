""" Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas."""

alunoMaisAlto = 0 
alunoMaisBaixo = 0
alturaMaisAlto = 0 
alturaMaisBaixo = 0 

for c in range(1, 11):
    numero = input(f'Digite número do aluno: ')
    altura = input(f'Digite a altura do aluno (em cm): ')

    if c == 1 or altura > alunoMaisAlto:
        alunoMaisAlto = numero
        alunoMaisBaixo = numero
        alturaMaisAlto = altura
        alturaMaisBaixo = altura
    if c == 1 or altura < alunoMaisBaixo:
        alunoMaisBaixo = numero
        alturaMaisBaixo = altura
        
print(f'O aluno mais alto é o: {alunoMaisAlto}, com {alturaMaisAlto}m de altura.')
print(f'O aluno mais baixo é o: {alunoMaisBaixo}, com {alturaMaisBaixo}m de altura.')