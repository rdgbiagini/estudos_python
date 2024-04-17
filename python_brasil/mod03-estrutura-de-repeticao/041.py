""" Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67

"""
from time import sleep



divida = float(input('Informe valor da dívida: '))
print('PROCESSANDO: [. . . . . ]')
sleep(1)

semJuros = divida
tresP = divida * 1.10
seisP = divida * 1.15
noveP = divida * 1.20
dozeP = divida * 1.25

parcela1 = semJuros / 1
parcela3 = tresP / 3
parcela6 = seisP / 6
parcela9 = noveP / 9
parcela12 = dozeP / 12

print('VEJA ABAIXO AS CONDIÇÕES PARA PAGAMENTO DESSA DÍVIDA: ')
sleep(1)
print(f"""
VALOR DA DÍVIDA     VALOR DOS JUROS     QUANTIDADE DE PARCELAS      VALOR DAS PARCELAS

{semJuros:.2f}              0%                      01                  {divida:.2f}
{tresP:.2f}                10%                      03                  {parcela3:.2f}
{seisP:.2f}                15%                      06                  {parcela6:.2f}
{noveP:.2f}                20%                      09                  {parcela9:.2f}
{dozeP:.2f}                25%                      12                  {parcela12:.2f}

""")
