""" 
A população do país A seja de 80000 habitantes com uma taxa anual de crescimento de 3%; 
A população do país B seja de 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. """

from time import sleep

popA = 80000
popB = 200000

crescA = 0.030 
crescB = 0.015

ano = 0

while popA <= popB:
    popA = int(popA + (popA * crescA))
    popB = int(popB + (popB * crescB))
    print(f'Após {ano} ano(s) A tem {popA} habitantes e B tem {popB} habitantes, portanto A ainda não passou.')
    ano += 1
    sleep(0.3)

print(f'Após {ano} anos a população de A ({popA}) ultrapassa ou iguala a população de B ({popB}). ')