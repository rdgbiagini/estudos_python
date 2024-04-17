""" Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 

As perguntas são:
01 - "Telefonou para a vítima?"
02 - "Esteve no local do crime?"
03 - "Mora perto da vítima?"
04 - "Devia para a vítima?"
05 - "Já trabalhou com a vítima?" 

Depois dessas perguntas esse programa deve emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente". """

# LEMBRO QUE TEM UMA FORMA DE FAZER O ARMAZENAMENTO DAS RESPOSTAS EM UMA LISTA. E DEPOIS SOMAR AS QUANTIDADES DE "S" e "N" DADAS PELO USUÁRIO. 

print('RESPONDA APENAS "S" PARA SIM OU "N" PARA NÃO')

# PRIMEIRO ESTAMOS ARMAZENANDO AS RESPOSTAS COMO "VAZIAS" PARA SE TER UMA VARIÁVEL QUE SE BUSCA ACHAR COM O LAÇO "FOR" DE BAIXO. 

q1 = ''
q2 = ''
q3 = ''
q4 = ''
q5 = ''

# AQUI DEVEMOS ACUMULAR A QUANTIDADE DE "SIM" E "NÃO" DADA PELO USUÁRIO, PORÉM, AO FINAL, VAMOS USAR APENAS A QUANTIDADE DE SIM, ENTÃO A SOMANÃO PODERÁ SER IGNORADA ATÉ.

somaSim = somaNao = 0

# AQUI FIZ UM "FOR" PARA QUE AS PERGUNTAS SEJAM FEITAS, DENTRO DE UM RANGE, DE 1 A 5, PARA QUE AS PERGUNTAS SEJAM FEITAS DE FORMA GRADATIVA, JÁ QUE A IDEIA AQUI É ESTUDAR O "FOR".
# FOI FEITO PARA CADA RANGE UMA PERGUNTA DIFERENTE. SE TIVESSEMOS MAIS PERGUNTAS, FARÍAMOS MAIS LINHAS APENAS. 
# PODERIA TE FEITO DIRETO, SEM O FOR, PORÉM, A IDEIA AQUI É ESTUDAR O "FOR" MESMO.

for q in range(1,6):
    if q == 1:
        q1 = str(input('Telefonou para a vítima? [   ] ')).upper().strip()
    elif q == 2:
        q2 = str(input('Esteve no local do crime? [   ] ')).upper().strip()
    elif q == 3:
        q3 = str(input('Mora perto da vítima? [   ] ')).upper().strip()
    elif q == 4:
        q4 = str(input('Devia para a vítima? [   ] ')).upper().strip()
    elif q == 5:
        q5 = str(input('Já trabalhou para a vítima? [   ] ')).upper().strip()

if q1 in 'Ss':
    somaSim += 1
if q2 in 'Ss':
    somaSim += 1
if q3 in 'Ss':
    somaSim += 1
if q4 in 'Ss':
    somaSim += 1
if q5 in 'Ss':
    somaSim += 1

print(somaSim)
print(somaNao)
print(q1, q2, q3, q4, q5)

if somaSim == 1 or somaSim == 2:
    print(f'\33[33mSUSPEITO!\033[m')
elif somaSim == 3 or somaSim == 4:
    print(f'\33[35mCÚMPLICE!\033[m')
if somaSim == 5:
    print(f'\33[31mCULPADO!\033[m')
