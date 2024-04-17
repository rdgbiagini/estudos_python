""" Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido """

sexo = input('Digite "F" para Feminino ou "M" para Masculino: [   ] ').strip().upper()

if sexo == 'Ff':
   print('O sexo é feminino.')

elif sexo == 'Mm':
    print('O sexo é masculino.')

else: 
    print('Sexo inválido.')

#Se fizer 2 ifs e não if + elif ele vai pular e considerar que o else se usa também. E vai aparecer 2 informações quando se precisa de 1. 