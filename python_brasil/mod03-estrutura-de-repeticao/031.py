""" O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. 
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. 
Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.
"""

# ==================================================================================================================================================================================== #
# AQUI MANTEVE O OTÁRIO DO MANOEL, MAS AO MENOS MUDOU A QUESTÃO UM POUCO PARA TAPEAR. VAMOS NESSA.
# ==================================================================================================================================================================================== #

contProdutos = 0
somaProdutos = 0 
troco = 0 

# ==================================================================================================================================================================================== #
# PRIMEIRO DEVE RECEBER NO PROGRAMA UM NÚMERO ILIMITADO DE PRODUTOS E SEUS PREÇOS, OU SEJA, UM "while True" PARA RECEBER NOME DO PRODUTO E SEU PREÇO. 
# ==================================================================================================================================================================================== #

while True:
    preco = float(input('PREÇO DO PRODUTO: [ DIGITE 0 - PARA ENCERRAR O PROGRAMA ]: '))
    contProdutos += 1
    somaProdutos += preco
    if preco == 0:
        break

# ==================================================================================================================================================================================== #
# AQUI JÁ FORA DO LAÇO WHILE PERGUNTAMOS SOBRE O PREÇO PARA FAZERMOS A CONTA DO TROCO E APRESENTAR O RESULTADO FINAL ESPERADO. 
# ==================================================================================================================================================================================== #

print(f'Foram no total {contProdutos:.2f} produtos, com o preço de R$ {somaProdutos:.2f}.')
dinheiro = float(input('Quanto o cliente pagou? '))

troco = dinheiro - somaProdutos

print(f'Uma vez que o cliente pagou {dinheiro:.2f}, o troco é {troco:.2f}.')