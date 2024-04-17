""" Desenvolva uma lógica que calcule, com base no peso e altura da pessoa o seu IMC (Índice de massa corpórea) e e diga: 
Abaixo de 18.5 está abaixo do seu peso.
Entre 18.5 e 25 está no seu peso ideal.
25 até 30 está com sobre peso.
30 a 40 tem obesidade. 
Acima de 40 está com obesidade mórbida. """

peso = float(input('Informe peso: [em kg] '))
altura = float(input('Informe altura: [em m] '))
imc = (peso / (altura * altura))

if imc < 18.5:
    print('abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print('peso ideal')
elif imc >= 25 and imc < 30:
    print('sobrepeso.')
elif imc >= 30 and imc < 40:
    print('obesidade.')
else: 
    print('\33[1;30;41mCOLÉ, GORDO! VAI CORRER, DESGRAÇA. MAS SÓ SE QUISER CHEGAR ATÉ O FINAL DO ANO.\33[m ')