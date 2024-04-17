""" Crie um programa que leia uma frase e diga: 
Quantas letras "a"
Onde aparece a primeira
Onde aparece a última
Tudo em uma única frase """

frase = str(input('Digite uma frase: ')).upper().strip()

print(f'A letra "A" aparece {frase.count("A")} vezes na frase')
print(f'A primeira letra "A" apareceu na posição {frase.find("A") + 1}.')
print(f'A última letra "A" apareceu na posição {frase.rfind("A") + 1}.')