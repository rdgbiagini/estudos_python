""" Crie um programa que tenha uma função fatorial() que recebe dois parâmetros, sendo o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico 
(opcional) indicando se será mostrado ou não na tela o processo de cálculo de fatorial. """

def fatorial(num=1, show=0):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

f1 = fatorial(5, True)
f2 = fatorial(4, False)
f3 = fatorial()

print(f'{f1}, {f2} e {f3}.')