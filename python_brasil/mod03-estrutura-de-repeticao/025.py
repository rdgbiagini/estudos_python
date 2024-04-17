""" Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; 
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada. """

listaNome = []
listaIdade = []
contPessoas = 0
somaIdades = 0
situacaoSala = ' '

while True:
    cont = str(input('Deseja inserir mais alguém? (S / N)? '))
    if cont in 'Nn':
        break
    else:
        nome = str(input('Nome: '))
        listaNome.append(nome)
        contPessoas += 1
        idade = int(input('Idade: '))
        listaIdade.append(idade)
        somaIdades += idade
        mediaIdades = (somaIdades) / (contPessoas)
    if mediaIdades < 25:
        situacaoSala = 'sala de pessoas jovens'
    elif mediaIdades > 25 and mediaIdades < 60:
        situacaoSala = 'sala de pessoas de idade adulta'
    elif mediaIdades > 60:
        situacaoSala = 'sala de idosos'

print(f'Fora inseridos {contPessoas} na lista, totalizando uma média de idade de {mediaIdades} anos, portanto temos uma {situacaoSala}.')
