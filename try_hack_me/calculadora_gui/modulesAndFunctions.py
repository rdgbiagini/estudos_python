# ==================================================================================================================================================================== #
# ESTE ARQUIVO DEVERA CONTER TODAS AS "def" E PARTES GENERICAS DO PROGRAMA PRINCIPAL DA CALCULADORA.
# ==================================================================================================================================================================== #

# ==================================================================================================================================================================== #
# PARTE ESTETICA E DE CORES DA APLICACAO E FORMATACAO DOS MENUS E DA CALCULADORA EM GERAL
# ==================================================================================================================================================================== #

linhaAzul = "\33[34m=\33[m" * 180
linhaBranca = "=" * 180
linhaAmarela = "\33[33m=\33[m" * 180
linhaVermelha = "\33[31m=\33[m" * 180

tituloMenuInicial = ("\33[33mBEM VINDO AO MENU INICIAL DA SUA CALCULADORA!\33[m").center(180)
tituloCalculadora = ("\33[33mVOCE ESTA AGORA NA VISUALIZACAO DA CALCULADORA!\33[m").center(180)

# ==================================================================================================================================================================== #
# FUNCAO PRINCIPAL DA CALCULADORA. PRINCIPAL PROPOSITO DE CRIACAO DESSA APLICACAO.
# TEM QUE SER FEITA UMA CALCULADORA ETERNA, ONDE SE PARE DE FAZER AS CONTAS E IMPRIMIR NA TELA APENAS QUANDO O USUARIO ACIONAR A IGUALDADE NA TELA OU NO COMANDO
# ==================================================================================================================================================================== #

def calculadoraAcumuladora():
    
    contValor = 1
    acumulador = 0

    while True:
        valor = input(f'INSIRA {contValor}° VALOR OU "=" PARA ENCERRAR: ')
        contValor += 1

        if valor.lower() == '=':
            print(f"RESULTADO FINAL ACUMULADO: {acumulador}")
            break

        try:
            valor = float(valor)
        except ValueError:
            print("VALOR INVALIDO! INSIRA UM NUMERO OU '=' PARA ENCERRAR.")
            continue

        operacao = input('INSIRA OPERACAO VALIDA ("+", "-", "*", "/", "**"): ')

        if operacao not in ('+', '-', '*', '/', '**'):
            print("OPERACAO INVALIDA! INSIRA UMA OPERACAO VALIDA.")
            continue

        if operacao == '+':
            acumulador += valor
        elif operacao == '-':
            acumulador -= valor
        elif operacao == '*':
            acumulador *= valor
        elif operacao == '/':
            if valor == 0:
                print("NAO E POSSIVEL DIVIDIR POR ZERO!")
                continue
            acumulador /= valor
        elif operacao == '**':
            acumulador **= valor
        
        print(f"RESULTADO: {acumulador}")

# ==================================================================================================================================================================== #
# ACESSO AO MENU DA MEMORIA DA CALCULADORA, QUE DEVE TER ESSAS PARTICULARIDADES:  
# ==================================================================================================================================================================== #

def memoriaCalculadora():
    print(linhaBranca)    

def backupCalculadora(): 
    print(linhaBranca)
    
# ==================================================================================================================================================================== #
# ESTA FUNCAO E A ABERTURA DA CALCULADORA, DO PROGRAMA E GERACAO DE UM MENU BASICO, MENU GENERICO PARA A CALCULADORA.
# ==================================================================================================================================================================== #

def menuInicial():
    print(linhaAmarela)
    print(linhaAzul)
    print(tituloMenuInicial)
    print(linhaAzul)
    print(linhaAmarela)
    print()
    opcMI = int(input("""
\33[34mAQUI VOCE PODE ACESSAR: 

\33[33m[ 1 ]\33[m \33[34mCALCULADORA\33[m
\33[33m[ 2 ]\33[m \33[34mMEMORIA\33[m 
\33[33m[ 3 ]\33[m \33[34mBACKUP\33[m 

\33[34m[   ]:\33[m """))
    
    if opcMI == 1:
        calculadoraAcumuladora()
    elif opcMI == 2:
        memoriaCalculadora()
    elif opcMI == 3: 
        backupCalculadora()
    else:
        menuInicial()