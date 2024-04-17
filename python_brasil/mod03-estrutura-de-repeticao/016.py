""" A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500. """

def fibonacci(n):
    fibSequence = []
    a, b = 0, 1
    
    while len(fibSequence) < n:
        if a >= 10000:
            break
        else: 
            fibSequence.append(a)
            a, b = b, a + b
        
    return fibSequence


# SOLICITAR DO USUÁRIO A QUANTIDADE DE TERMOS

n = int(input("Digite QUANTIDADE de termos: "))

# CHAMAR A FUNÇÃO E MOSTRAR NA TELA.

fibSequence = fibonacci(n)
print(fibSequence)
