""" Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 (zero) termos. """

print('GERADOR DE P.A.')
print('===' * 15)

primeiro = int(input('PRIMEIRO TERMO: '))
razao = int(input('DIGITE RAZÃO: '))
termo = primeiro
cont = 1
mais = 10
total = 0

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} --> ', end=' ')
        termo += razao
        cont += 1 
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos')
print('FIM!')
