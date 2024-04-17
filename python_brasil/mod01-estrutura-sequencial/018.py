""" Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps). 
Calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). """

tamanho = float(input('Qual o tamanho (em MB) do programa? '))
velocidade = float(input('Qual a velocidade (em MBps) da conexão? '))

espera = tamanho / velocidade

print(f'O tempo de espera será de {espera} segundos.')