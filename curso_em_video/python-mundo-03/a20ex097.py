""" Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 
Exemplo: "escreva(Olá Mundo!)" Saída: --- Olá Mundo! --- (mas esses traços são em cima e em baixo, ou seja, ele quer que a função receba * a quantidade de len(escreva) + alguma coisa). """

def escreva(txt):
    print('=' * (len(txt) + 2))
    print(txt)
    print('=' * (len(txt) + 2))

escreva('paralelepipedo')