""" Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. """

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input('DIGITE VALOR: '))
if is_prime(num):
    print(f"{num} é primo.")
else:
    print(f"{num} não é primo.")
