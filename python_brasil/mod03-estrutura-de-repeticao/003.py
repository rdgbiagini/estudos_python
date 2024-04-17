""" Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'; """

# NOME TEM QUE SER MAIOR QUE 3 CARACTERES. 

nome = str(input('NOME: '))
while len(nome) < 3:
    nome = str(input('NOME: '))

# IDADE TEM QUE SER ENTRE 0 E 150. 

idade = int(input('IDADE: '))
while idade < 0 or idade > 150:
    idade = int(input('IDADE: '))

# SALARIO TEM QUE SER MAIOR DO QUE ZERO. 

salario = int(input('SALÁRIO: '))
while salario < 0:
    salario = int(input('SALÁRIO: '))

# SEXO TEM QUE SER SEMPRE M OU F

sexo = str(input('SEXO (S/F): '))
while sexo not in 'FfMm':
    sexo = str(input('SEXO (S/F): '))

# ESTADO CIVIL TEM QUE SER UMA DAS INICIAIS, S, C, V OU D.

esCivil = str(input('ESTADO CIVIL (S / C / V / D): '))
while esCivil not in 'SsCcVvDd':
    esCivil = str(input('ESTADO CIVIL (S / C / V / D): '))