""" Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: 01 - Quantidade de notas / 02 - A 
maior nota / 03 - A menor nota / 04 - A média da turma / 05 - A situação (opcional). Adicione também as docStrings da função.  """

def notas(*n, sit=False):
    
    """ Essa função receberá uma ou várias notas de um determinado aluno, retornando a média dessas notas e, se quiser, a situação final desse aluno ao final do ano. """
    
    r = dict()

    r['TOTAL'] = len(n)
    r['MAIOR'] = max(n)
    r['MENOR'] = min(r)
    r['MÉDIA'] = sum(n) / len(n)

    if sit:
        if r['MÉDIA'] >= 7:
            r['SITUAÇÃO'] = 'BOA!'
        elif r['MÉDIA'] >= 5:
            r['SITUAÇÃO'] = 'MEDIANA'
        else:
            r['SITUAÇÃO'] = 'HORRÍVEL'

# PROGRAMA PRINCIPAL

notas(5.5, 2.5, 1.5, sit=True)


