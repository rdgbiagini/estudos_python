""" Crie um programa onde o usuário possa digitar 7 valores numéricos (for in range) e cadastre-os em uma lista única, que nos mostre separadamente os valores pares e ímpares. 
No final mostre os valores pares e ímpares em ordem crescente.  """

num = [[], []] # UMA LISTA ÚNICA GRANDONA QUE TEM QUE TER 2 LISTAS DENTRO (UMA PAR E OUTRA ÍMPAR)

valor = 0 # ESTAMOS ATRIBUINDO ZERO PARA DEPOIS CAPTAR UM A UM POIS SABEMOS O RANGE QUE QUEREMOS.

for c in range(1, 8): #ESTÁ SE UTILIZANDO "1 A 8" PARA NÃO TER UM "ÍTEM 0" APENAS
    valor = int(input(f'{c}º VALOR: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

# ATÉ AQUI EU TINHA FEITO TUDO CERTINHO, INCLUSIVE COM A MESMA LINHA DE RACIOCÍNIO DO GUANABARA. DEPOIS, O QUE EU NÃO ACERTEI FAZER FOI ENTENDER A LÓGICA DO ".sort()".
# NA REALIDADE, FOI SABER COMO FUNCIONA A ORDEM DO SORTE NESSA APLICAÇÃO, MAS AGORA SIM, COLOCAR ANTES DO PRINT FORMATADO PARA DEPOIS IMPRIMIR ELE JÁ COM O ".sort()" FEITO. 

num[0].sort()
num[1].sort()
print(num)
print(num[0])
print(num[1])