""" Crie um programa que vai ler vários números e criar uma lista. Depois disso crie duas listas extras, sendo a primeira contendo os valores pares digitados e a segunda contendo os 
valores ímpares digitados pelo usuário. 
Ao final mostre na tela o conteúdo das três listas geradas. No primeiro loop faça só a leitura dos valores, depois, nos outros loops faça as análises e separação de qual número deverá 
ir para qual lista. 
Não precisa ser em ordem crescente ou decrescente, mas se for, ainda melhor. O usuário deverá dizer na hora que deve parar de alimentar o sistema de números. """

# CRIANDO UMA LISTA QUE SERÁ TOTALMENTE INCLUÍDA PELO USUÁRIO. 

numsTodos = []
numsPar = []
numsImpar = []

while True:
    num = int(input('NÚMERO: '))
    numsTodos.append(num)
    resp = str(input('CONTINUAR? [S/N]? '))
    if resp in 'Nn':
        break

for c in range(0, len(numsTodos)):
    verif = numsTodos[c]
    if verif % 2 == 0:
        numsPar.append(verif)
    else:
        numsImpar.append(verif)

print(f'A LISTA FOI: {numsTodos}')
print(f'OS PARES SÃO: {numsPar}')
print(f'OS ÍMPARES SÃO: {numsImpar}')
    
