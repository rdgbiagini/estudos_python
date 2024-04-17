""" Faça um Programa que verifique se uma letra digitada é vogal ou consoante. """

letra = str(input('Digite uma letra: '))

if letra in ['a', 'e', 'i', 'o', 'u']:
    print('É uma vogal.')
else:
    print('É uma consoante.')