""" Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                  Até 5 Kg           Acima de 5 Kg

Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00:
Receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
Escreva o valor a ser pago pelo cliente. """

# PARÂMETROS BÁSICOS

morango = float(input('Quantos kg de morango? [   ]'))
maca = float(input('Quantos kg de maça? [   ]'))

totalMorango = ()
totalMaca = ()

# CÁLCULOS

preco1Morango = 2.5
preco2Morango = 2.2

if morango <= 5:
    totalMorango = morango * preco1Morango
    print(totalMorango)
elif morango > 5 and morango < 8:
    totalMorango = morango * preco2Morango
    print(totalMorango)
else:
    totalMorango = (morango * preco2Morango) * 0.9
    print(totalMorango)

preco1Maca = 1.8
preco2Maca = 1.5

if maca <= 5:
    totalMaca = maca * preco1Maca
    print(totalMaca)
elif maca > 5 and maca < 8:
    totalMaca = maca * preco2Maca
    print(totalMaca)
else:
    totalMaca = (maca * preco2Maca) * 0.9
    print(totalMaca)