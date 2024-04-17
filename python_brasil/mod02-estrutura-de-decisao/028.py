""" O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção.Não há limites para Carne. 

Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 

Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere:

Cupom fiscal, contendo: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. """

# PARÂMETROS BÁSICOS

print('BOM DIA. BEM VINDO AO HIPERMERCADO TABAJARA.')

fileDuplo1 = 4.9
fileDuplo2 = 5.8

alcatara1 = 5.9
alcatara2 = 6.8

picanha1 = 6.9
picanha2 = 7.8

carne = float(input('Informe qual a carne que você quer: 1 - Filé Duplo / 2 - Alcatara / 3 - Picanha.'))
kg = float(input('Informe quantos kg de carne quer levar.'))

# TOTAL A PAGAR E IF PARA DESCOBRIR POR TIPO DE CARNE. 

total = ()

if carne == 1 and kg <= 5:
    total = fileDuplo1 * kg
    print(f'Você escolheu {kg}kg de {carne}.')
elif carne == 1 and kg >5:
    total = fileDuplo2 * kg
    print(f'Você escolheu {kg}kg de {carne}.')
elif carne == 2 and kg <= 5:
    total = alcatara1 * kg
    print(f'Você escolheu {kg}kg de {carne}.')
elif carne == 2 and kg > 5:
    total = alcatara2 * kg
    print(f'Você escolheu {kg}kg de {carne}.')
elif carne == 3 and kg <= 5:
    total = picanha1 * kg
    print(f'Você escolheu {kg}kg de {carne}.')
elif carne == 3 and kg > 5:
    total = picanha2 * kg
    print(f'Você escolheu {kg}kg de {carne}.')

cartao = float(input('Você vai pagar com cartão Tabajara? 1 - SIM / 2 - NÃO. [   ]'))

if cartao == 1:
    total = total * 0.95
else: 
    total = total 