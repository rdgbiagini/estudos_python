""" Refaça o desafio 051, lendo o primeiro termo e a razão de uma Progressão Aritmética, mostrando os 10 primeiros termos da progressão usando a estrutura "while". """

""" Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. """

print('GERADOR DE P.A.')
print('===' * 15)

primeiro = int(input('PRIMEIRO TERMO: '))
razao = int(input('DIGITE RAZÃO: '))
termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo} --> ', end=' ')
    termo += razao
    cont += 1 
    
print('FIM!')
