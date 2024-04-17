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

somaSim = 0

q1 = str(input('Telefonou para a vítima? [   ] ')).upper().strip()
q2 = str(input('Esteve no local do crime? [   ] ')).upper().strip()
q3 = str(input('Mora perto da vítima? [   ] ')).upper().strip()
q4 = str(input('Devia para a vítima? [   ] ')).upper().strip()
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

if somaSim == 1 or somaSim == 2:
    print('SUSPEITO!')
elif somaSim == 3 or somaSim == 4:
    print('CÚMPLICE!')
if somaSim == 5:
    print('CULPADO!')