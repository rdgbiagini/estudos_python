""" Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. """

data = input('Digite uma data no formato dd/mm/aaaa: ')

# DEF GERA UMA FUNÇÃO DENTRO DO PYTHON PARA VALIDAR VÁRIOS PONTOS.

def validData(data):
    try:
        day, month, year = map(int, data.split('/'))
        if day < 1 or day > 31 or month < 1 or month > 12 or year < 1:
            return False

        if month in [4, 6, 9, 11] and day > 30:
            return False

        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                if day > 29:
                    return False
            elif day > 28:
                return False

        return True
    except ValueError:
        return False

if validData(data):
    print("A data é válida!")
else:
    print("A data é inválida!")