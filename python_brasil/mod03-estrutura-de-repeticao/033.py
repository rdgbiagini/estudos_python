""" O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior 
temperaturas informadas, bem como a média das temperaturas. """

# PROGRAMA QUE LEIA CONJUNTO INDETERMINADO DE TEMPERATURAS
# MENOR
# MAIOR
# MÉDIA

contTemperaturas = 1
maior = 0
menor = 0
somaTemperaturas = 0 

while True:
    temp = str(input('Inserir nova temperatura? (S / N) '))
    if temp in 'Nn':
        break
    else:
        celsius = int(input(f'Informe {contTemperaturas}ª temperatura º C? '))
        contTemperaturas += 1
        somaTemperaturas += celsius

if contTemperaturas == 1:
    maior = celsius
    menor = celsius
else:
    if celsius > maior:
        maior = celsius
    elif celsius < menor:
        menor = celsius

mediaTemperaturas = somaTemperaturas / (contTemperaturas - 1)

print(f'Foram informados {contTemperaturas - 1} temperaturas diferentes.')
print(f'A soma de todas as temperaturas informadas é de {somaTemperaturas}.')
print(f'A média das temperaturas é de {mediaTemperaturas}.')
print(f'A maior temperatura informada foi {maior}.')
print(f'A menor temperatura informada foi {menor}.')