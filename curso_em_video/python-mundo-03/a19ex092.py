""" Crie um programa que leia um nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de zero, o dicionário 
receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. 60 anos para mulher e 65 anos para homens. """

from datetime import datetime

peao = dict()

peao['NOME'] = str(input('NOME: ')).strip()
peao['ANO'] = int(input('ANO NASC: '))
peao['IDADE'] = datetime.now().year - peao['ANO']
peao['SEXO'] = str(input('SEXO (M / F): '))
peao['CTPS'] = int(input('Nº CTPS: (000 - PARA NÃO TENHO CTPS) '))
if peao['CTPS'] != 0:
    peao['CONTRATO'] = int(input('ANO DE CONTRATO: '))
    peao['SALÁRIO'] = float(input('SALÁRIO RECEBIDO: '))
    peao['APOSENTADORIA'] = peao['IDADE'] + ((peao['CONTRATO'] + 35) - datetime.now().year)

print(peao)

