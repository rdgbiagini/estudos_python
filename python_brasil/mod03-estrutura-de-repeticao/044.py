""" Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

"""
totVotos = 0 
contCandidato01 = 0 
contCandidato02 = 0
contCandidato03 = 0 
contCandidato04 = 0
contNulo = 0

contBranco = 0

print("""
=======================
CANDIDATOS:
=======================
1 - CANDIDATO 01
2 - CANDIDATO 02
3 - CANDIDATO 03
4 - CANDIDATO 04
5 - VOTO NULO
6 - VOTO EM BRANCO """)

while True:
    voto = int(input('Qual seu voto? (Digite 0 para encerrar a votação.):  '))
    if voto == 0:
        break
    if voto == 1:
        totVotos += 1
        contCandidato01 += 1
    elif voto == 2:
        totVotos += 1
        contCandidato02 += 1
    elif voto == 3:
        totVotos += 1
        contCandidato03 += 1
    elif voto == 4:
        totVotos += 1
        contCandidato04 += 1
    elif voto == 5:
        totVotos += 1
        contNulo += 1
    elif voto == 6:
        totVotos += 1
        contBranco += 1

percentagemNulosSobreTotal = 100 * (contNulo / totVotos)
percentagemBrancosSobreTotal = 100 * (contBranco / totVotos)

print(f'Candidato 01 teve {contCandidato01} votos.')
print(f'Candidato 02 teve {contCandidato02} votos.')
print(f'Candidato 03 teve {contCandidato03} votos.')
print(f'Candidato 04 teve {contCandidato04} votos.')
print(f'O número de votos nulos foi {contNulo}.')
print(f'O número de votos em branco foi {contBranco}.')
print(f'A percentagem de votos nulos sobre o total de votos é {percentagemNulosSobreTotal:.2f}%.')
print(f'A percentagem de votos em branco sobre o total de votos é {percentagemBrancosSobreTotal:.2f}%.')