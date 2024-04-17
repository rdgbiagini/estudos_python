""" Crie um programa em que o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final serão exibidos 
todos os valores únicos dessa lista, em ordem crescente.  """

listaNum = list()
segue = ''

while True: 
    add = int(input('DIGITE NÚMERO: '))
    listaNum.append(add)
    segue = input('CONTINUAR INSERINDO NÚMEROS? [ "S" / "N" ]:  ').strip().upper()
    if segue in 'Nn':
        break

print(f'A lista digitada foi {listaNum}. ')