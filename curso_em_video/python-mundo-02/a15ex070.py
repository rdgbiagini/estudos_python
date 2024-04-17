""" Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai continuar cadastrando.
No final, mostre: Qual o total gasto na compra? / Quantos produtos custam mais de 1000.00 reais? Qual o nome do produto mais barato? """

# VARIÁVEIS QUE USAREMOS NA APLICAÇÃO. PRODUTO, PREÇO E QUANTIDADE. 

contador = 0 

# A DIFERENÇA DA MINHA SOLUÇÃO PARA A DO GUANABARA É QUE ELE METEU UM CONTADOR LOGO DE CARA, PORQUE DESSE CONTADOR ELE TERÁ UM "NORTE" PARA SABER AS COMPARAÇÕES DOS PREÇOS. 

quantProduto = 0
precoTotal = 0 
produtoAcima1000 = 0
maisBarato = 0
produtoMaisBarato = ''

# "WHILE TRUE" PARA COLETAR DADOS INFINITAMENTE, ATÉ QUE O USUÁRIO DIGA QUE NÃO QUER MAIS. 

while True:
    produto = str(input('O QUE COMPROU? ')).strip().capitalize()
    preco = int(input('QUANTO CUSTOU? '))
    contador += 1
    precoTotal += preco

    if preco >= 1000:
        produtoAcima1000 += 1
    
    if contador == 1:
        maisBarato = preco
        produtoMaisBarato = produto
    else:
        if preco < maisBarato:
            maisBarato = preco
            produtoMaisBarato = produto
    
    cont = str(input('CONTINUAR CADASTRANDO? [ "S" / "N" ]: ')).strip().upper()
    if cont in 'Nn':
        break

print(f'Foram comprados {quantProduto} produtos. ')
print(f'Foram gastos no total {precoTotal}. ')
print(f'Foram comprados {produtoAcima1000} produtos acima de R$ 1,000.00 nessa compra. ')
print(f'O produto mais barato custou {maisBarato} e foi o {produtoMaisBarato}. ')

# AQUI É UM BOM EXERCÍCIO DE ANINHAMENTO, POIS TEMOS TRÊS "IF" DENTRO DE UM "WHILE TRUE" COM A COLETA DE INFORMAÇÕES DIVERSAS.
