""" Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são: 
Imposto de Renda, que depende do salário bruto (conforme tabela abaixo);
3% para o Sindicato 
FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:

Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00 """

# BIBLIOTECAS A SEREM CARREGADAS

import math

# CÁLCULO DO VALOR DE HORA X MÊS PARA SE ENCONTRAR SALÁRIO. DEPOIS CÁLCULO DO SALÁRIO BRUTO. 

hora = float(input('Qual o valor de sua hora trabalhada? '))
mes = float(input('Quantas horas você trabalhou nesse mês? '))
salarioBruto = float(mes * hora)
math.ceil(salarioBruto) # ARREDONDANDO PRA CIMA O VALOR DO SALÁRIO PARA CASO SEJA COLOCAO UM VALOR QUEBRADO NA CONTA
print(f'Já que você trabalhou {mes} horas esse mês, a um valor de {hora} X hora, seu salário bruto foi de {salarioBruto}.')
print(f'Então você vai receber BRUTO R$ {hora * mes} nesse mês. ')

# AGORA PARA DESCOBRIR A ALÍQUOTA DE IR A SER DESCONTADA DO PEÃO:

aliquotaIr = ()

if salarioBruto <= 900:
    aliquotaIr = salarioBruto * 0
elif salarioBruto > 900 and salarioBruto <= 1500:
    aliquotaIr = salarioBruto * 0.05
elif salarioBruto > 1500 and salarioBruto <= 2500:
    aliquotaIr = salarioBruto * 0.10
else:
    aliquotaIr = salarioBruto * 0.20

print(f'Já que o seu salário é de {salarioBruto}, o seu desconto de IR é igual a {aliquotaIr}.')

# AGORA VAMOS CALCULAR O INSS E O FGTS DO PEÃO: 

inss = 0.10
descontoInss = salarioBruto * inss

fgts = 0.11
descontoFgts = salarioBruto * fgts

# TOTAIS DESCONTOS: 

totalDescontos = descontoInss 
salarioLiquido = salarioBruto - totalDescontos

print(f'Considerando o seu salário de {salarioBruto}, o seu desconto do INSS desse mês é de {descontoInss}.')
print('\nEntão temos:')

# AQUI ENTÃO ESTAMOS COMPILANDO TODAS AS INFORMAÇÕES DO FUNCIONÁRIO DESSE MÊS 

print(f'Salário Bruto ({hora} * {mes}): R$ {salarioBruto}')
print(f'(-) IR (): R$ {aliquotaIr}')
print(f'(-) INSS (10%): R$ {descontoInss}')
print(f'FGTS (11%): R$ {descontoFgts}')
print(f'Total de descontos: R$ {totalDescontos}')
print(f'Salário Líquido: R$ {salarioLiquido} ')