""" Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar de ler quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram inseridos e qual foi a soma entre eles. (desconsiderando a flag de parada) """

contador = 0 
media = 0 

while True:
    n = int(input('DIGITE VALOR: '))
    if n == 999:
        break
    contador += 1
    media += n

print(f'''Foram inseridos {contador} números.
A média entre eles é {media // contador} ''')