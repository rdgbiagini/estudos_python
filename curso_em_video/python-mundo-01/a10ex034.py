""" Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento:
Para salários superiores a R$ 1,250.00 calcule um aumento de 10%.
Para salários inferiores ou iguais o aumento é de 15%.  """

salario = float(input('\33[0;30;41mDigite seu salário:\33[m '))
reajuste = ()

if salario <= 1250:
    reajuste = '15%'
    salarioNovo = salario * 1.15
else:
    reajuste = '10%'
    salarioNovo = salario * 1.10

print(f'seu salário antigo era {salario}, logo seu reajuste é de {reajuste}, assim, seu salário novo é de {salarioNovo}')