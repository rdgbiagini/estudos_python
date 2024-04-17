""" Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com parênteses abertos e 
fechados na ordem correta. Pode ser uma expressão matemática por exemplo.  """

exp = input('EXPRESSÃO: ')
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('.')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            break

if len(pilha) == 0:
    print('Sua expressão está correta.')
else:
    print('Expressão inválida.')
