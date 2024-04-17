# ==================================================================================================================================================================== #
# CADASTRO DE CLIENTES = DADOS: NOME, RAZAO SOCIAL, ENDEREçO, PESSOA RESPONSAVEL, TELEFONE, FREQUENCIA DE PEDIDOS, TIPO DE PEDIDOS, FATURAS EM ABERTO, PREçO
# LEMBRETE DE PEDIDOS, AGENDAMENTOS DE PEDIDOS
# LINK 01 = https://www.youtube.com/watch?v=Oq2ekGfKmx8
# LINK 02 = https://www.youtube.com/watch?v=pybXmHvXRZg
# ==================================================================================================================================================================== #

# ==================================================================================================================================================================== #
# TELA INICIAL / BIBLIOTECAS IMPORTADAS / CORES USADAS NA APLICAçAO
# ==================================================================================================================================================================== #

import tkinter as tk

vermelho = '#a30517'
preto = '#0a0001'
azul = '#020270'

# ==================================================================================================================================================================== #

jnl = tk.Tk() # CRIA A JANELA
jnl.title("CADASTRO DE CLIENTES")
jnl.geometry("1000x500") # LARGURA X ALTURA
jnl.resizable(False, False)

# 3. Adicione os componentes da interface, como rótulos, campos de entrada e botões.

# ==================================================================================================================================================================== #

def saveClient():
    
    """ A ideia dessa funçao è salvar todos os dados que foram incluidos pelo usuario 
    E na sequencia, devera enviar tudo para dentro do sistema no arquivo em excel. """
    
    cliente = entCliente.get()
    cnpj = entCnpj.get()
    shopping = entShopping.get()
    endereco = entEndereco.get()
    resposavel = entResponsavel.get()
    telefone = entTelefone.get()
    email = entEmail.get()

# ==================================================================================================================================================================== #

# Aqui você pode salvar os dados do cliente em um banco de dados ou arquivo

# ==================================================================================================================================================================== #

lblCliente = tk.Label(jnl, text="CLIENTE:", font='Calibri 12', width=50)
lblCliente.pack()

entCliente = tk.Entry(jnl, width=80)
entCliente.pack(anchor='center')

# ==================================================================================================================================================================== #

lblCnpj = tk.Label(jnl, text="CNPJ:", font='Calibri 12', width=50)
lblCnpj.pack()

entCnpj = tk.Entry(jnl, width=15)
entCnpj.pack()

# ==================================================================================================================================================================== #

lblShopping = tk.Label(jnl, text="SHOPPING:", font='Calibri 12', width=50)
lblShopping.pack()

entShopping = tk.Entry(jnl)
entShopping.pack()

lstShoppings = tk.Listbox(jnl)
lstShoppings.pack()

opcoes = ["Opcao 1", "Opcao 2", "Opcao 3"]

# opcoes = ["Barra", "Bela Vista", "Iguatemi", "Itaigara", "Norte Shopping", "Paralela", 
#        "Paseo", "Piedade", "Pituba Parque Center", "Salvador", "Sao Cristovao", 
#        "Hospital Aliança", "Hospital Irma Dulce"]

for o in opcoes:
    lstShoppings.insert(tk.END, opcoes)

# ==================================================================================================================================================================== #

lblEndereco = tk.Label(jnl, text="ENDEREçO:", font='Calibri 12', width=50)
lblEndereco.pack()

entEndereco = tk.Entry(jnl, width=100)
entEndereco.pack()

# ==================================================================================================================================================================== #

lblResponsavel = tk.Label(jnl, text="RESPONSAVEL PELO PEDIDO:", font='Calibri 12', width=50)
lblResponsavel.pack()

entResponsavel = tk.Entry(jnl, width=80)
entResponsavel.pack()

# ==================================================================================================================================================================== #

lblTelefone = tk.Label(jnl, text="TELEFONE:", font='Calibri 12', width=50)
lblTelefone.pack()

entTelefone = tk.Entry(jnl, width=15)
entTelefone.pack()

# ==================================================================================================================================================================== #

lblEmail = tk.Label(jnl, text="E-MAIL:", font='Calibri 12', width=50)
lblEmail.pack()

entEmail = tk.Entry(jnl, width=80)
entEmail.pack()

# ==================================================================================================================================================================== #

btSalvarCliente = tk.Button(jnl, text="INCLUIR CLIENTE", command=saveClient)
btSalvarCliente.pack()

# ==================================================================================================================================================================== #
# COMANDO QUE EXECUTA E INICIA A JANELA DO PROGRAMA
# ==================================================================================================================================================================== #

jnl.mainloop()

