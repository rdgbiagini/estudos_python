""" Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal. """

# Eu sei que aqui existe uma forma de fazer isso com a biblioteca math, mas eu deixei assim que é para, quando estiver com Gui
# a gente revisar tudo e eu tentar lembrar de como usar essa biblioteca. 
# Lembro também que isso pode reduzir bastante o código com todo esse if abaixo. 

num1 = float(input('Digite valor 01: [   ]: '))
num2 = float(input('Digite valor 02: [   ]: '))

print('Agora informe, qual operação você deseja fazer: ')

calc = float(input('1 - soma / 2 - subtração / 3 - multiplicação / 4 - divisão: [   ]: '))

soma = ()
subtracao = ()
multiplicacao = ()
divisao = ()

if calc == 1:
    soma = num1 + num2
    print(f'{soma}')
elif calc == 2:
    subtracao = num1 - num2
    print(f'{subtracao}')
elif calc == 3:
    multiplicacao = num1 * num2
    print(f'{multiplicacao}')
elif calc == 4:
    divisao = num1 / num2
    print(f'{divisao}')
else:
    print('Opção inválida. Tente novamente depois.')