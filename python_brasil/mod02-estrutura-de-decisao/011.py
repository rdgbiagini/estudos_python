""" As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa.
Esse programa calculará os reajustes: 
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento. """

salario = float(input('Informe seu salário (em R$): '))
salarioNovo = ()
reajuste = ()

if salario <= 280:
    salarioNovo = salario * 1.20
    reajuste = '20%'
elif salario > 280 and salario <= 700:
    salarioNovo = salario * 1.15
    reajuste = '15%'
elif salario > 700 and salario <= 1500:
    salarioNovo = salario * 1.10
    reajuste = '10%'
else: 
    salarioNovo = salario * 1.05
    reajuste = '5%'

print(f'Seu salário era de {salario}, seu reajuste será de {reajuste}, e assim, vai passar a ser de {salarioNovo}.')