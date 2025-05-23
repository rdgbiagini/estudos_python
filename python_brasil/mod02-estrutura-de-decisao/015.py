""" Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes."""

lado1 = float(input('Informe lado 01: '))
lado2 = float(input('Informe lado 02: '))
lado3 = float(input('Informe lado 03: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('Sim, é possível se fazer um triângulo com estes valores.')

if lado1 == lado2 == lado3:
    print('Esse triângulo é equilátero.')
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print('Esse triângulo é isóceles.')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('Esse triângulo é escaleno.')