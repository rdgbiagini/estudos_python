"""113 - Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora nela a possibilidade de digitação de um número de tipo inválido. Aproveite e crie também uma 
função leiaFloat() com a mesma funcionalidade. """

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[31mERRO. Por favor, digite um número inteiro válido. \33[m')
            continue
        except (KeyboardInterrupt):
            print('\33[31mERRO! Entrada interrompida pelo usuário.\33[m')
            return n
        else:
            return n 
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\33[31mERRO. Por favor, digite um número inteiro válido. \33[m')
            continue
        except (KeyboardInterrupt):
            print('\33[31mERRO! Entrada interrompida pelo usuário.\33[m')
            return n
        else:
            return n 


n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')

print(f'O valor inteiro digitado foi \33[33m{n1}\33[m e o valor real foi \33[33m{n2}\33[m')
