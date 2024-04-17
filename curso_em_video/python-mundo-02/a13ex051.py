""" Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão. """

termo = int(input('DIGITE \33[34mTERMO\33[m DA P.A.: [   ] '))
razao = int(input('DIGITE \33[34mRAZÃO\33[m DA P.A.: [   ] '))
decimo = termo + (10 - 1) * razao

for c in range(termo, decimo + 1, razao):
    print(c, end=' -> ')
print('ACABOU!')