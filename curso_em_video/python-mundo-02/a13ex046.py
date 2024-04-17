""" Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artifícios. Indo de 10 a 0, com uma pausa de 1 segundo entre eles. """

from time import sleep

for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('BOM! POW! KABUM!! \33[7;37;40mFeliz ano novo. \33[m')