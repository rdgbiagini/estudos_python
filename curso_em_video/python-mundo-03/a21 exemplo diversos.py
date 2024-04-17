def contador(i, f, p):
    
    """
    i = inicio
    f = fim
    p = passo
    return = no return
    
    """

    c = i
    while c <= f:
        print(f'{c}', end='.. ')
        c += p
    print('FIM!')

contador(2, 10, 2)