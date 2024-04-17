""" Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. """

# ============================================================================================================================================================ #
# UM CONTADOR PARA CADA CANDIDATO, POR ISSO SÓ 4 OPÇÕES, PARA SÓ TER QUE FAZER 4 "if"
# ============================================================================================================================================================ #

contAdamastor = 0
contCarlinhosPadoca = 0 
contDeraldo = 0 
contZeGalinha = 0 
eleito = ' '

totEleitores = int(input('São quantos eleitores? [   ] ')) # DETERMINA O TAMANHO DO LAÇO QUE VAI PEDIR A CONTAGEM DE VOTOS

# ============================================================================================================================================================ #
# INÍCIO DO LAÇO FOR PARA FAZER A VOTAÇÃO DE ELEITOR POR ELEITOR. COLOCANDO O NÚMERO DO ELEITOR AINDA.
# ============================================================================================================================================================ #

for e in range(1, totEleitores + 1):
    
    print(f'\33[31m{e}º ELEITOR:\33[m ')
    voto = int(input('''Em quem deseja votar? 

[ 1 ] ADAMASTOR
[ 2 ] CARLINHO DA PADOCA
[ 3 ] DERALDO
[ 4 ] ZÉ GALINHA

[   ]: '''))
    
    if voto == 1:
        contAdamastor += 1
    elif voto == 2:
        contCarlinhosPadoca += 1
    elif voto == 3:
        contDeraldo += 1
    elif voto == 4:
        contZeGalinha += 1

# ============================================================================================================================================================ #
# AQUI FALAMOS FORA DO LAÇO FOR POR SER JÁ SOBRE A PARTE POSTERIOR A VOTAÇÃO.
# ============================================================================================================================================================ #

if contAdamastor > contCarlinhosPadoca and contAdamastor > contDeraldo and contAdamastor > contZeGalinha:
    eleito = 'ADAMASTOR!'
elif contCarlinhosPadoca > contAdamastor and contCarlinhosPadoca > contDeraldo and contCarlinhosPadoca > contZeGalinha:
    eleito = 'CARLINHOS DA PADOCA!'
elif contDeraldo > contAdamastor and contDeraldo > contCarlinhosPadoca and contDeraldo > contZeGalinha:
    eleito = 'DERALDO!'
elif contZeGalinha > contAdamastor and contZeGalinha > contCarlinhosPadoca and contZeGalinha > contDeraldo:
    eleito = 'ZÉ GALINHA!'

print(f'O candidato Adamastor teve {contAdamastor} votos.')
print(f'O candidato Carlinhos da Padoca teve {contCarlinhosPadoca} votos.')
print(f'O candidato Deraldo teve {contDeraldo} votos.')
print(f'O candidato Zé Galinha teve {contZeGalinha} votos.')

print(f'Portanto, o candidato eleito foi {eleito}.')