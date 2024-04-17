""" Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. 
Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio. """

# =========================================================================================================================================================================== #
# INFORMAÇÕES GERAIS QUE SE PRECISA 
# =========================================================================================================================================================================== #

maiorIndiceAcidentes = 0
menorIndiceAcidentes = 0
contCidades = 1

somaVeiculosCidades = 0 
somaAcidentesCidades = 0

# =========================================================================================================================================================================== #
# INÍCIO DO CÓDIGO
# =========================================================================================================================================================================== #

for cidades in range(1, 6): 
    
    codCidade = int(input('Digite código da cidade: '))
    contCidades += 1
    numVeiculos1999 = int(input('Digite quantidade de veículos de passeios em 1999: '))
    somaVeiculosCidades += numVeiculos1999 #LOOP QUE GERA A INFORMAÇÃO PARA TOTAL DE CARROS NAS CIDADES PARA QUE SEJA POSSÍVEL FAZER O CÁLCULO A MÉDIA
    numAcidentes1999 = int(input('Digite quantidade de acidentes com vítimas, também em 1999: '))
    somaAcidentesCidades += numAcidentes1999 #LOOP QUE GERA A INFORMAÇÃO PARA TOTAL DE ACIDENTES PARA QUE SEJA POSSÍVEL FAZER O CÁLCULO DA MÉDIA

    if cidades == 1:
        maiorIndiceAcidentes = codCidade
        menorIndiceAcidentes = codCidade
    else:
        if numAcidentes1999 > maiorIndiceAcidentes:
            maiorIndiceAcidentes = numAcidentes1999
        elif numAcidentes1999 < menorIndiceAcidentes:
            menorIndiceAcidentes = numAcidentes1999

mediaVeiculos = somaVeiculosCidades / (contCidades - 1) # COMO SABEMOS QUE SERÁ 5 CIDADES JÁ PODE FAZER A MÉDIA SOBRE 5 MAS PODERIA TAMBÉM TER UM CONTADOR.
mediaAcidentesCidades = somaAcidentesCidades / (contCidades - 1) # COMO SABEMOS QUE SERÁ 5 CIDADES JÁ PODE FAZER A MÉDIA SOBRE 5 MAS PODERIA TAMBÉM TER UM CONTADOR.

print(f'A cidade com mais carros é: {codCidade}.')
print(f'A cidade com mais acidentes é: {codCidade}.')
print(f'A média de carros é {mediaVeiculos}.')
print(f'A média de acidentes é de {mediaAcidentesCidades}')


