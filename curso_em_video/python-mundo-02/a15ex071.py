""" Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início pergunte ao usuário qual o valor sacado (número inteiro - esse caixa não saca moedas).
Então o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa tem cédulas de 50, 20, 10 e 1 """

# VARIÁVEIS A SEREM COLETADAS

saque = 0
conf = 0

# CONTADORES DE NOTAS 

nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota1 = 0

# INÍCIO DA INTERAÇÃO COM USUÁRIO. PRIMEIRO PEDIR VALOR A SER SACADO. 

saque = int(input('DIGITE VALOR DO SAQUE: R$ [   ]  '))
conf = saque 

# ESSE "IF" ESTÁ AQUI PARA CONFERIR SE O VALOR A SER SACADO ESTÁ SENDO UM VALOR VÁLIDO, OU SEJA, UM VALOR POSITIVO, ACIMA DE 0 E INTEIRO. 

if saque <= 0:
    saque = int(input(f'Operação Inválida. Digite valor válido. [   ]  '))
else: 
    conf = saque

# A PARTIR DAQUI SE ESTÁ TESTANDO SE O VALOR É MAIOR QUE O VALOR DAS NOTAS PARA PODER CONTAR QUANTAS NOTAS DE CADA VALOR DE FORMA OTIMIZADA
# MENOR QUANTIDADE DE NOTAS POSSÍVEIS. 

while conf > 0:
    while conf >= 100:
        nota100 += 1
        conf -= 100
    while conf >= 50: 
        nota50 += 1
        conf -= 50
    while conf >= 20:
        nota20 += 1
        conf -= 20
    while conf >= 10: 
        nota10 += 1
        conf -= 10
    while conf >= 5:
        nota5 += 1
        conf -= 5
    while conf >= 1:
        nota1 += 1
        conf -= 1

# RELATÓRIO FINAL DO SAQUE INFORMANDO VALOR SOLICITADO E A QUANTIDADE DE NOTAS EMITIDAS POR TIPO DE NOTA. 

print(f'''Foi (ram) emitida(s):
      {nota100} nota(s) de R$ 100.00; 
      {nota50} nota(s) de R$ 50.00; 
      {nota20} nota(s) de R$ 20.00; 
      {nota10} nota(s) de R$ 10.00; 
      {nota5} nota(s) de R$ 5.00; 
      {nota1} nota(s) de R$ 1.00 para o saque solicitado no valor de R$ {saque}.''')