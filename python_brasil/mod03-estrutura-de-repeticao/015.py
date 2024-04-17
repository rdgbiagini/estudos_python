""" A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo. """

def fibonacci(n):
    fibSequence = []
    a, b = 0, 1
    
    while len(fibSequence) < n:
        fibSequence.append(a)
        a, b = b, a + b
    
    return fibSequence


# SOLICITAR DO USUÁRIO A QUANTIDADE DE TERMOS

n = int(input("Digite QUANTIDADE de termos: "))

# CHAMAR A FUNÇÃO E MOSTRAR NA TELA.

fibSequence = fibonacci(n)
print(fibSequence)
