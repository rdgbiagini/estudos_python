""" Desenvolva um programa que leia 4 valores pelo teclado e guarde em uma tupla. No final mostre quantas vezes aparece o valor 9 / Qual foi a posição em que apareceu o 
primeiro valor 3 / Quais foram os números pares? / IMPORTANTE QUE se buscar um valor que não existe, o programa deverá indicar isso com um erro.  """

num = (int(input('DIGITE NÚMERO: [  ] ')),
       int(input('DIGITE OUTRO NÚMERO: [  ] ')),
       int(input('DIGITE MAIS UM NÚMERO: [  ] ')),
       int(input('DIGITE ÚLTIMO NÚMERO: [  ] ')))

print(num)

if 9 in num:
    print(f'Você digitou o valor 9 {num.count(9)} vezes. ')
else:
    print('Você não digitou o valor 9 nenhuma vez. ')

if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição. ')
else:
    print(f'O valor 3 não foi digitado.')

for n in num:
    if n % 2 == 0:
        
        print(f'Os valores pares digitados, foram: {n}' , end=' ')
    else:
        print('Não foram digitados números pares. ')