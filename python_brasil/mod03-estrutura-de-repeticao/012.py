""" Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. 
A saída deve ser conforme o exemplo abaixo:

Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50 """

from time import sleep

while True:
    n = int(input('Digite valor entre 1 e 10: '))
    if n < 1:
        print('\33[31mERRO! Tente novamente com um valor válido (entre 1 e 10) seu ANIMAL!\33[m')
    elif n > 10:
        print('\33[31mERRO! Tente novamente com um valor válido (entre 1 e 10) seu ANIMAL!\33[m')
    else:
        break

print(f'Ok, veremos a taboada de {n} abaixo:')
sleep(1)
print('=' * 40)
sleep(1)

for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
    sleep(0.2)

sleep(1)
print('=' * 40)

