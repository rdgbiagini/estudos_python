# ==================================================================================================================================================================== #
# CALCULADORA SIMPLES COM AS 4 OPERACOES BASICAS POR ENQUANTO.
# https://www.youtube.com/watch?v=pdy3nh1tn6I
# ==================================================================================================================================================================== #

# ==================================================================================================================================================================== #
# DEFINE THE FUNCTIONS NEEDED --> ADD, SUB, MULT, DIV.
# PRINT OPTIONS TO THE USER
# ASK FOR VALUES
# CALL THE FUNCTIONS
# WHILE LOOP TO CONTINUE THE PROGRAM UNTIL THE USER WANT TO END IT
# PRINT THE RESULTS
# ==================================================================================================================================================================== #

def add(a, b):
    answer = a + b
    print("\n" + str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print("\n" + str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a, b):
    answer = a * b
    print("\n" + str(a) + " * " + str(b) + " = " + str(answer) + "\n")
    
def div(a, b):
    answer = a / b
    print("\n" + str(a) + " / " + str(b) + " = " + str(answer) + "\n")

def pot(a, b):
    answer = a ** b
    print("\n" + str(a) + " **" + str(b) + " = " + str(answer) + "\n")

# ==================================================================================================================================================================== #
# ESSE CODIGO FOI ESCRITO PELO PROFESSOR DO CURSO. ELE PRIMEIRO FEZ O CODIGO COM AS FUNCOES E DEPOIS FEZ O "if" GRANDAO ABAIXO PRA CHAMAR AS FUNCOES. 
# O PONTO E QUE DEPOIS DISSO FEITO ELE CRIOU ESSE "while True" AQUI EMBAIXO E JOGOU TUDO DENTRO, TANTO O MENU QUANTO O "choice" E O "if" GRANDAO.
# ==================================================================================================================================================================== #

while True: 
    
    print("A. Addiction")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Input your choice: ")

    if choice == "a" or choice == "A": # FEITO ASSIM PARA SEGUIR O VIDEO E A AULA MAS EU FARIA COM: "if choice in 'Aa':" QUE REDUZ BEM O CODIGO. TODAS AS "IFS"
        print("Addiction")
        a = int(input("Input first number (a): "))
        b = int(input("input second number (b): "))
        add(a, b)
    elif choice == "b" or choice == "B": 
        print("Subtraction")
        a = int(input("Input first number (a): "))
        b = int(input("Input second number (b): "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Input first number (a): "))
        b = int(input("Input second number (b): "))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Division") 
        a = int(input("Input first number (a): "))
        b = int(input("Input second number (b): "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Exit program.")
        quit()