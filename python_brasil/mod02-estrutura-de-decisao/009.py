""" Faça um Programa que leia três números e mostre-os em ordem decrescente. """

num1 = int(input('Informe número 01: '))
num2 = int(input('Informe número 02: '))
num3 = int(input('Informe número 03: '))

numeros = [num1, num2, num3]
numeros.sort(reverse=True)

#Lembrar de, quando fizer uma lista meter colchetes e escrever os valores dos títulos sem aspas que não precisa.
#O "sort" faz a lista estar em uma ordem, no caso crescente, enquanto o "reverse=True" faz a lista ser decrescente.
#O valor "True" dentro de reverse é que dá todo o resultado nesse caso. 

print(numeros)