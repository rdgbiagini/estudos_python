""" Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo, que mostre na tela algumas informações geradas pelas funções que já temos no módulo 
criado até aqui. """

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

def resumo(preco=0, taxaA=10, taxaR=5):
    print('\33[31m=\33[m' * 50)
    print('\33[31mRESUMO DO VALOR\33[m'.center(50))
    print('\33[31m=\33[m' * 50)
    print(f'PREÇO ANALISADO: {moeda(preco)}'.center(50))
    print('\33[31m=\33[m' * 50)
    print(f'DOBRO DO PREÇO: \t\33[33m{dobro(preco, True)}\33[m'.center(50))
    print(f'AUMENTANDO 20%: \t\33[33m{aumentar(preco, 20, True)}\33[m'.center(50))
    print(f'DIMINUINDO 15%: \t\33[33m{diminuir(preco, 20, True)}\33[m'.center(50))
    print(f'METADE DO PREÇO: \t\33[33m{metade(preco, True)}\33[m'.center(50))
    print('\33[31m=\33[m' * 50)