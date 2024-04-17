""" Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, conseno e da tangente desse ângulo. """

# IMPORTAÇÃO DE BIBLIOTECAS, NO CASO A BIBLIOTECA "MATH" DO PYTHON QUE VEM PARA FAZER OS CÁLCULOS JÁ PRONTOS. NO CASO ESPECIFICAMENTE SOBRE ESTAS FUNÇÕES DENTRO DA BIBLIOTECA MATH.

from math import radians, sin, cos, tan

# ÚNICA INFORMAÇÃO QUE A GENTE PRECISA QUE SEJA INSERIDA PELO USUÁRIO, QUE É O GRAU DO ÂNGULO. 

angulo = float(input('Digite o ângulo que você deseja: '))

#CÁLCULOS DO SENO, COSSENO E TANGENTE FEITAS DIRETAMENTE PELA BIBLIOTECA. NESSE CASO COMO SE IMPORTA DA BIBLIOTECA, NÃO PRECISA COLOCAR MATH.SIN E SIM APENAS SIN() PARA ACESSAR A FUNÇÃO

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'Com esse ângulo temos um seno de {seno:.2f}, um cosseno de {cosseno:.2f} e uma tangente de {tangente:.2f}.')