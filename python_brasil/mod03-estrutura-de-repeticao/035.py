""" Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário. """
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_list(n):
    prime_list = []
    for num in range(2, n + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

# Obter entrada do usuário
num = int(input("Digite um número inteiro: "))

# Gerar a lista de números primos
primes = generate_prime_list(num)

# Exibir a lista de números primos
print("Números primos entre 1 e", num, ":")
print(primes)
