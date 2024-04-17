""" Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se a pessoa 
tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições. """

def voto(a):
    
    from datetime import date

    calcIdade = (date.today().year) - a

    if calcIdade <= 16:
        return 'VOTO NEGADO. VAI PRA CASA, CRIANÇA.'
    elif calcIdade <= 18:
        return 'VOTO FACULTATIVO. VAI BEBER E ESQUECE ESSA MERDA.'
    elif calcIdade <= 65:
        return 'VOTO OBRIGATÓRIO, SE FUDEU!'
    else:
        return 'VOTO FACULTATIVO DE NOVO. VAI PRA CASA DESCANSAR E ESQUEÇE ESSA MERDA.'

voto(1940)