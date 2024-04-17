""" Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal. 
Use a seguinte fórmula: (72.7*altura) - 58 """

alt = float(input('Informe a altura da pessoa (em metros): '))

pesoIdeal = (72.7 * alt) - 58

print(f'Para essa pessoa, seu peso ideal é até {pesoIdeal}')