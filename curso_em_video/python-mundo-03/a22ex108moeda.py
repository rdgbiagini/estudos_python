""" Adapte o código do Desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado. """

def aumentar(preco=0, taxa=0):
    
    """ 
    Essa função recebee 2 parâmetros:
    
    --> preco = Valor base sobre o qual deverá ser feita a operação. 
    --> taxa = Taxa sobre a qual será aumentado do x inicial para se obter um resultado. 
    --> Se não for informado qualquer dos parâmetros, o padrão é 0.

    Exemplo: "aumentar(10, 4):" fará a soma de 10 com 4 e apresentará este resultado. 
    
    """
    r = preco + (preco * (taxa/100))
    return r
    # print(f"O valor {preco} aumentado de {taxa} tem como resultado {r}.")

def diminuir(preco=0, taxa=0):
    
    """ 
    Essa função recebee 2 parâmetros:
    
    --> preco = Valor base sobre o qual deverá ser feita a operação.
    --> taxa = Valor que será diminuído do x inicial para se obter um resultado. 
    --> Se não for informado qualquer dos parâmetros, o padrão é 0.

    Exemplo: "diminuir(10, 4):" fará a subtração de 10 com 4 e apresentará este resultado. 
    
    """
    r = preco - (preco * (taxa/100))
    return r
    # print(f"O valor {preco} aumentado de {taxa} tem como resultado {r}.")

def dobro(preco=0):
    
    """ 
    Essa função recebee apenas um parâmetro:
    
    --> preco = Valor base sobre o qual deverá ser feita a operação.
    --> Se não for informado o parâmetro, o padrão é 0. 
    
    Exemplo: "dobro(10):" fará a multiplicação de 10 por 2 e apresentará este resultado, o seu dobro. 
    
    """
    r = preco * 2
    return r
    # print(f'O dobro do valor {x} tem como resultado {r}.')

def metade(preco=0):
    
    """ 
    Essa função recebee apenas um parâmetro:
    
    --> preco = Valor base sobre o qual deverá ser feita a operação.
    --> Se não for informado o parâmetro, o padrão é 0. 
    
    Exemplo: "metade(10):" fará a divisão de 10 por 2 e apresentará este resultado, a sua metade. 
    
    """
    r = preco / 2
    return r
    # print(f'A metade do valor {preco} tem como resultado {r}.')

def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:^8.2f}'.replace('.', ',')
