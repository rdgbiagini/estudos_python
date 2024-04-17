""" Escreva um programa para análise de crédito bancário para a compra de uma casa.
O programa deverá perguntar o valor da casa que se quer comprar.
Depois o salário que o comprador tem. Depois quantos anos ele pretende quitar o valor. Considere para isso a taxa de juros de 0% (não incidência de taxas).
Calcule o valor da prestação mensal. Se ela passar de 30% do valor do salário mensal do comprador não deverá aprovar o crédito. 
Deverá apresentar uma mensagem verde para a aprovação e uma vermelha para a reprovação do crédito por parte do comprador. """

from time import sleep

titulo = 'ANÁLISE DE CRÉDITO BANCÁRIO'

print('=' * (len(titulo) * 2))
print('\33[34mANÁLISE DE CRÉDITO BANCÁRIO :\33[m')
print('\33[30m=' * (len(titulo) * 2) + '\n')

# AQUI VAMOS JUNTAR TODAS AS INFORMAÇÕES QUE A GENTE PRECISA PARA ANÁLISE DO CRÉDITO. 

casa = float(input('\33[31mCASA: R$\33[m '))
salario = float(input('\33[31mSALÁRIO: R$\33[m '))
prazo = float(input('\33[31mMESES P/ PAGAMENTO?\33[m '))
print('\33[1;30;41mPROCESSANDO [. . . ]\33[m')

sleep(3)

# CÁLCULOS

juros = '0%'

print(f'A taxa de juros aplicada será de {juros}')

sleep(3)

mensal = casa / prazo # CÁLCULO DO VALOR MENSAL. ESSE NÃO PODE SUPERAR 30% DO VALOR DO SALÁRIO DO COMPRADOR. 

print(f'A prestação mensal será de: {mensal}')

print('=' * (len(titulo) * 2))
print('\33[34mCALCULANDO CRÉDITO PARA FINANCIAMENTO [. . . . . ] :\33[m')
print('\33[30m=' * (len(titulo) * 2) + '\n')

sleep(3)

if mensal >= salario * 0.3:
    print('\33[1;30;41mCRÉDITO REPROVADO. TENTE NOVAMENTE COM OUTROS VALORES.\33[m')
else:
    print('\33[0;30;42mCRÉDITO APROVADO! PARABÉNS!\33[m')
