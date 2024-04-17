""" Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool: 

até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

Gasolina:

até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro.

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
depois calcule e imprima o valor a ser pago pelo cliente.
Sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. """

combustivel = float(input('Qual o combustível a ser abastecido? Digite "1" - alcool ou "2" = gasolina: [   ]  '))
litros = float(input('Quantos litros? '))

alcool = 1.90

descAMenos20Litros = 0.03 #3% em multiplicação
descAMais20Litros = 0.05 #5% em multiplicação

gasolina = 2.50

descGMenos20Litros = 0.04 #4% em multiplicação
descGMais20Litros = 0.06 #6% em multiplicação

if combustivel == 1 and litros <= 20:
    print(f'O valor do alcool é {alcool}. Seu desconto é de 3%, portanto seu valor final é de {((alcool * litros) - (alcool * descAMenos20Litros))}')
elif combustivel == 1 and litros > 20:
    print(f'O valor do alcool é {alcool}. Seu desconto é de 5%, portanto seu valor final é de {((alcool * litros) - (alcool * descAMais20Litros))}')

if combustivel == 2 and litros <= 20:
    print(f'O valor do alcool é {gasolina}. Seu desconto é de 4%, portanto seu valor final é de {((gasolina * litros) - (gasolina * descGMenos20Litros))}')
elif combustivel == 2 and litros > 20:
    print(f'O valor do alcool é {gasolina}. Seu desconto é de 6%, portanto seu valor final é de {((gasolina * litros) - (gasolina * descGMais20Litros))}')
