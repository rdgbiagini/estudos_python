""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados: 
11% para o Imposto de Renda;
8% para o INSS; 
5% para o sindicato.

Faça um programa que nos dê:
Salário bruto.
Quanto pagou ao INSS.
Quanto pagou ao sindicato.
Salário líquido.
Calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido. """

hora = float(input('Qual o valor de sua hora trabalhada? '))
mes = float(input('Quantas horas você trabalhou nesse mês? '))

print(f'Então você vai receber BRUTO R$ {hora * mes} nesse mês. ')

ir = (mes * 0.11)
inss = (mes * 0.08) 
sindicato = (mes * 0.05)

liquido = mes - ir - inss - sindicato

print(f'+ SALÁRIO BRUTO: R$ {mes}')
print(f'- IR (11%): R$ {ir}')
print(f'- INSS (8%): R$ {inss}')
print(f'- SINDICATO (5%): R$ {sindicato}')
print(f'+ SALÁRIO LÍQUIDO: R$ {liquido}')
