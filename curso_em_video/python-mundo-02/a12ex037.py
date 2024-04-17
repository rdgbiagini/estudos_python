""" Escreva um programa que leia um número inteiro qualquer e peça para o usuário qual a base da conversão, sendo: 
1 para binário / 2 para octal / 3 para haxadecimal.
Usando o hífen alinhado. """

# O PYTHON TEM NATIVAMENTE A MAIORIA DAS FUNÇÕES QUE VOCÊ MAIS USA, NÃO SERIA DIFERENTE COM ISSO. TEMOS BINÁRIO, OCTAL E HEXADECIMAL COMO FUNÇÃO INSERIDA NA BASE DO PYTHON MESMO. 

n = int(input('Informe Número: '))
conversao = int(input('Como deseja converter esse número? 1 - binário; 2 - octal; 3 - hexadecimal. '))
nConvertido = ()

if conversao == 1:
    nConvertido = bin(n)
    print(f'O número informado foi {n} e a conversão para binário torna ele no {nConvertido}.')
elif conversao == 2:
    nConvertido = oct(n)
    print(f'O número informado foi {n} e a conversão para octal torna ele no {nConvertido}.')
elif conversao == 3:
    nConvertido = hex(n)
    print(f'O número informado foi {n} e a conversão para hexadecimal torna ele no {nConvertido}.')
else: 
    print('\33[1;30;41mOPÇÃO INVÁLIDA, FDP! ESCREVE CERTO ESSA PORRA, CARALHO!!!\33[m')