""" Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condições de pagamento. 
À vista, dinheiro ou cheque tem desconto de 10%.
à vista no cartão tem desconto de 5%.
Em até 2x no cartão é o preço normal. 
Acima de 2x no cartão tem que acrescentar 20% de juros.  """

produto = float(input('Digite valor do produto: '))
forma = int(input('''Como vai ser pago?
    [ 1 ] à vista, dinheiro ou cheque? - 10%  
    [ 2 ] à vista no cartão de crédito? - 5%
    [ 3 ] em até 2x no cartão de crédito? - 0%
    [ 4 ] mais de 2x no cartão de crédito? + 20% \n'''))

pagamento = ()

if forma == 1:
    pagamento = produto * 0.9
    print(F'Seu preço é de {produto} e seu desconto é de 10%, então seu valor final é de R$ {pagamento}.')
elif forma == 2:
    pagamento = produto * 0.95
    print(F'Seu preço é de {produto} e seu desconto é de 5%, então seu valor final é de R$ {pagamento}.')
elif forma == 3: 
    pagamento = produto
    print(F'Seu preço é de {produto} e seu desconto é de 0%, então seu valor final é de R$ {pagamento}.')
elif forma == 4:
    pagamento = produto * 1.2
    print(F'Seu preço é de {produto} e seu acréscimo é de 20%, então seu valor final é de R$ {pagamento}.')
else: 
    print('\33[1;30;41mOPÇÃO INVÁLIDA, FDP! ESCREVE CERTO ESSA PORRA, CARALHO!!!\33[m')