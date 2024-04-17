""" Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex: apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona """

frase = str(input('DIGITE UMA FRASE: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, - 1, -1):
    inverso += junto[letra]
print(junto, inverso)

if inverso == junto:
    print('\33[1;33;41mTemos um palíndromo!\33[m')
else:
    print('Não é um palíndromo.')