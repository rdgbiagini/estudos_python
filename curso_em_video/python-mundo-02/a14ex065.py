""" Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor digitado.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar outros números.  """

# PRIMEIRO DEVEMOS CAPTAR O VALOR A SER INSERIDO PELO USUÁRIO DO SISTEMA. 

valor = 0

# ESSES SÃO OS CÁLCULOS QUE A GENTE VAI PRECISAR FAZER NO DECORRER DO PROGRAMA. 

media = 0
maior = 0 
menor = 0 
contador = 0
continuar = True

valor = int(input('DIGITE UM VALOR: '))
maior = valor
menor = valor
continuar = str(input('DESEJA CONTINUAR? "S" - SIM OU "N" - NÃO ')).strip().upper()
contador += 1
media += valor


while continuar in 'Ss':
    valor = int(input('DIGITE UM VALOR: '))
    continuar = str(input('DESEJA CONTINUAR? "S" - SIM OU "N" - NÃO ')).strip().upper()
    contador += 1
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f'Foram cadastrados {contador} números. ')
print(f'O maior valor é {maior}. ')
print(f'O menor valor é o {menor}')
print(f'A média entre eles é de {media // contador}')