""" Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões. 
O programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito 
da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A / 02 - B / 03 - C / 04 - D / 05 - E / 06 - E / 07 - D / 08 - C / 09 - B / 10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

""" 

from time import sleep

listaTotal = dict()
nota = 0 

def captNotas():

    while True:
        aluno = str(input('Informe seu nome: (DIGITE "ZZZ" PARA ENCERRAR A APLICAÇÃO) ')).upper().strip()
        
        if aluno in 'ZZZ':
            break

        print(f'Ok {aluno}, seja bem vindo(a) a correção da sua prova. Nos informe agora questão a questão, quais as suas respostas.')
        print('( . . . )')
        sleep(1)

        for r in range(1, 11):
            rspt = str(input(f"Digite {r}ª resposta (A, B, C, D ou E): ")).upper()

            if r == 1 and rspt in 'A':
                nota += 1
            if r == 2 and rspt in 'B':
                nota += 1
            if r == 3 and rspt in 'C':
                nota += 1
            if r == 4 and rspt in 'D':
                nota += 1
            if r == 5 and rspt in 'E':
                nota += 1
            if r == 6 and rspt in 'E':
                nota += 1
            if r == 7 and rspt in 'D':
                nota += 1
            if r == 8 and rspt in 'C':
                nota += 1
            if r == 9 and rspt in 'B':
                nota += 1
            if r == 10 and rspt in 'A':
                nota += 1

        print(f'O aluno {aluno} teve um total de {nota} acertos, totalizando a nota {nota}.')

        listaTotal['ALUNO'] = {aluno}
        listaTotal['NOTA'] = {nota}

        reiniciar = str(input('Deseja inserir outro aluno? (S / N): '))
        if reiniciar in 'Ss':
            captNotas()
        else:
            print('Obrigado. Volte sempre!')
            print(listaTotal)

captNotas()

