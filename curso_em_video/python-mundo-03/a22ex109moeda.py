""" Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda()
desenvolvida no desafio 108. """

def aumentar(preco=0, taxa=0, formato=False):
    
    """ 
    Essa função recebee 2 parâmetros:
    
    --> preco = Valor base sobre o qual deverá ser feita a operação. 
    --> taxa = Taxa sobre a qual será aumentado do x inicial para se obter um resultado. 
    --> Se não for informado qualquer dos parâmetros, o padrão é 0.
    --> Para um format = True ele formata na posição da "def moeda():".

    Exemplo: "aumentar(10, 4):" fará a soma de 10 com 4 e apresentará este resultado. 
    
    """
    r = preco + (preco * (taxa/100))
    return r if formato is False else moeda(r)

def diminuir(preco=0, taxa=0, formato=False):
    
    """ 
    Essa função recebee 2 parâmetros:
    
    --> preco = Valor base sobre o qual deverá ser feita a operação.
    --> taxa = Valor que será diminuído do x inicial para se obter um resultado. 
    --> Se não for informado qualquer dos parâmetros, o padrão é 0.
    --> Para um formato = True ele formata na posição da "def moeda():".

    Exemplo: "diminuir(10, 4):" fará a subtração de 10 com 4 e apresentará este resultado. 
    
    """
    r = preco - (preco * (taxa/100))
    return r if formato is False else moeda(r)

def dobro(preco=0, formato=False):
    
    """ 
    Essa função recebee apenas um parâmetro:
    
    --> preco = Valor base sobre o qual deverá ser feita a operação.
    --> Se não for informado o parâmetro, o padrão é 0. 
    --> Para um formato = True ele formata na posição da "def moeda():".
    
    Exemplo: "dobro(10):" fará a multiplicação de 10 por 2 e apresentará este resultado, o seu dobro. 
    
    """
    r = preco * 2
    return r if formato is False else moeda(r)

def metade(preco=0, formato=False):
    
    """ 
    Essa função recebee apenas um parâmetro:
    
    --> preco = Valor base sobre o qual deverá ser feita a operação.
    --> Se não for informado o parâmetro, o padrão é 0. ]
    --> Para um formato = True ele formata na posição da "def moeda():".
    
    Exemplo: "metade(10):" fará a divisão de 10 por 2 e apresentará este resultado, a sua metade. 
    
    """
    r = preco / 2
    return r if formato is False else moeda(r)

def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:^8.2f}'.replace('.', ',')
