""" Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax² + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores.
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; """

import math

print('Digite os valores de "a", "b" e "c" a serem aplicados na equação "ax2 + bx + c".')

a = int(input('Digite "a": '))

if a == 0:
    print('Para "a" = 0, essa equação não é de segundo grau, portanto, não poderá ser realizada nessa aplicação. ')

b = int(input('Digite "b": '))
c = int(input('Digite "c": '))


