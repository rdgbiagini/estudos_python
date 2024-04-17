""" Crie um módulo chamado moeda.py que tenha as funções incorporadas, aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esses módulos e use algumas 
dessas funções anteriores. """

def aumentar(preco, taxa):
    
    """ 
    Essa função recebee 2 parâmetros:
    
    --> preco = Valor base sobre o qual deverá ser feita a operação.
    --> taxa = Taxa sobre a qual será aumentado do x inicial para se obter um resultado. 

    Exemplo: "aumentar(10, 4):" fará a soma de 10 com 4 e apresentará este resultado. 
    
    """
    r = preco + (preco * (taxa/100))
    return r
    # print(f"O valor {preco} aumentado de {taxa} tem como resultado {r}.")

def diminuir(preco, taxa):
    
    """ 
    Essa função recebee 2 parâmetros:
    
    --> preco = Valor base sobre o qual deverá ser feita a operação.
    --> taxa = Valor que será diminuído do x inicial para se obter um resultado. 

    Exemplo: "diminuir(10, 4):" fará a subtração de 10 com 4 e apresentará este resultado. 
    
    """
    r = preco - (preco * (taxa/100))
    return r
    # print(f"O valor {preco} aumentado de {taxa} tem como resultado {r}.")

def dobro(preco):
    
    """ 
    Essa função recebee apenas um parâmetro:
    
    --> preco = Valor base sobre o qual deverá ser feita a operação.
    
    Exemplo: "dobro(10):" fará a multiplicação de 10 por 2 e apresentará este resultado, o seu dobro. 
    
    """
    r = preco * 2
    return r
    # print(f'O dobro do valor {x} tem como resultado {r}.')

def metade(preco):
    
    """ 
    Essa função recebee apenas um parâmetro:
    
    --> preco = Valor base sobre o qual deverá ser feita a operação.
    
    Exemplo: "metade(10):" fará a divisão de 10 por 2 e apresentará este resultado, a sua metade. 
    
    """
    r = preco / 2
    return r
    # print(f'A metade do valor {preco} tem como resultado {r}.')
