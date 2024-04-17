""" Faça um programa que leia duas notas de um aluno e calcule sua média mostrando uma mensagem no final, de acordo com a média dele. Sendo: 
Média abaixo de 5 reprovado.
Média entre 5 e 6.9 recuperação.
Média 7 a 9.9 aprovado.
Média 10 aprovado com louvor.  """

# CAPTAR AS NOTAS DE UM ALUNO 

n1 = float(input('nota 01: '))
n2 = float(input('nota 02: '))
media = ((n1 + n2) / 2)

if media <= 5:
    print('VOCÊ ESTÁ REPROVADO. ')
elif media > 5 and media <= 6.9:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO.')
elif media > 7 and media <= 9.9:
    print('VOCÊ ESTÁ APROVADO. PARABÉNS, VÁ CURTIR SUA LIBERDADE PROVISÓRIA.')
else: 
    print('APROVADO COM LOUVOR PELA MÉDIA 10! MEUS PARABÉNS E UMA EXCELENTE FÉRIAS.')