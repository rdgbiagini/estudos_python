""" Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso. """

turno = input('Qual o seu turno de estudos? Digite "M" para Matutino, "V" para Vespertino: [   ]')

if turno == 'M':
   print('BOM DIA!')

elif turno == 'V':
    print('BOA TARDE!')

else: 
    print('Turno inválido.')