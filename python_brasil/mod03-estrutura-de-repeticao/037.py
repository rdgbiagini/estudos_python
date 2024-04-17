""" Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte 
a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas 
e dos pesos dos clientes """

contAlunos = 1
maisAlto = 0
somaAlturas = 0 
maisBaixo = 0
maisGordo = 0 
maisMagro = 0 
somaPesos = 0 

while True: 
    codigo = int(input(f'Código do {contAlunos}º aluno? (0 para encerrar a aplicação): '))
    if codigo == 0:
        break
    else:
        contAlunos += 1
        altura = float(input('Sua altura: '))
        somaAlturas += altura
        peso = float(input('Seu peso: '))
        somaPesos += peso

        if contAlunos == 1:
            maisAlto = altura
            maisBaixo = altura
            maisGordo = peso
            maisMagro = peso
        else:
            if maisAlto < altura:
                maisAlto = altura
            elif maisBaixo < altura:
                maisBaixo = altura
            elif maisGordo < peso:
                maisGordo = peso
            elif maisMagro < peso:
                maisMagro = peso

mediaAlturas = somaAlturas / (contAlunos - 1)
mediaPesos = somaPesos / (contAlunos - 1)




print(f'O aluno mais gordo é: {maisGordo}')
print(f'O aluno mais magro é: {maisMagro}')
print(f'O aluno mais baixo é: {maisBaixo}')
print(f'O aluno mais alto é: {maisAlto}')
print(f'A média de alturas é: {mediaAlturas}')
print(f'A média de pesos é: {mediaPesos}')


