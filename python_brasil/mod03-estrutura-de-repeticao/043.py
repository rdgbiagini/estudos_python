"""
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado. """

print("""
====================================
ESTE É O CARDÁPIO DISPONÍVEL: 
====================================

    ÍTEM       CÓDIGO    PREÇO
      
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00 

""")

listaPedido = dict()
contItens = 0 

cachorroQuente = 1.20
totCachorroQuente = 0 
bauruSimples = 1.30
totBauruSimples = 0
bauruComOvo = 1.50 
totBauruComOvo = 0
hamburguer = 1.20 
totHamburguer = 0
cheeseburguer = 1.30 
totCheeseburguer = 0
refrigerante = 1.00 
totRefrigerante = 0 

while True: 
    escolha = int(input('Digite o código do ítem que deseja selecionar: (ESCOLHA O ITEM "-1" PARA ENCERRAR) '))
    contItens += 1
    quantidade = int(input('Informe quantidade desse item: '))
    if escolha == -1:
        break
    elif escolha == 100:
        totCachorroQuente += 1
        listaPedido[f'ITEM {contItens}'] = 'Cachorro Quente'
        listaPedido['PREÇO'] = 'R$ 1,20'
    elif escolha == 101:
        totBauruSimples += 1
        listaPedido[f'ITEM {contItens}'] = 'Bauru Simples'
        listaPedido['PREÇO'] = 'R$ 1,30'
    elif escolha == 102:
        totBauruComOvo += 1
        listaPedido[f'ITEM {contItens}'] = 'Bauru com Ovo'
        listaPedido['PREÇO'] = 'R$ 1,50'
    elif escolha == 103:
        totHamburguer +=1 
        listaPedido[f'ITEM {contItens}'] = 'Hamburguer'
        listaPedido['PREÇO'] = 'R$ 1,20'
    elif escolha == 104:
        totCheeseburguer += 1
        listaPedido[f'ITEM {contItens}'] = 'Cheeseburguer'
        listaPedido['PREÇO'] = 'R$ 1,30'
    elif escolha == 105:
        totRefrigerante += 1
        listaPedido[f'ITEM {contItens}'] = 'Refrigenrante'
        listaPedido['PREÇO'] = 'R$ 1,00'

print(listaPedido)

