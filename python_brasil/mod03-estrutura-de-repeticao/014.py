""" Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares. """

listaX = []
calcPar = 0 
calcImpar = 0

for n in range(1, 11):
    x = int(input(f'Digite {n}º valor inteiro: '))
    listaX.append(x)
    if x % 2 == 0:
        calcPar += x
    else:
        calcImpar += x

print(f'A lista de números inseridos, foi: {listaX}.')
print(f'A soma dos números pares é: {calcPar}.')
print(f'A soma dos números ímpares é: {calcImpar}.')