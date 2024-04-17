# ==================================================================================================================================================================== #
# ASK USER IF THEY WANT TO GENERATE A PASSWORD OR NOT
# IF THEY DO, ASK FOR THE PASSWORD LENGHT
# IF INITIAL ANSWER IS "NO" CLOSE THE PROGRAM
# MAKE A LIST OF NUMBERS
# MAKE A LIST OF LETTERS
# MAKE A LIST OF SPECIAL SIGNS
# GENERATE THE PASSWORD
# PRINT THE PASSWORD
# ==================================================================================================================================================================== #

# ==================================================================================================================================================================== #
# IMPORTACAO DE BIBLIOTECAS PARA O USO NESSA APLICAçAO POR MAIS SIMPLES QUE POSSA PARECER PRECISA DE 2 BIBLIOTECAS. 
# CRIADAS AS LISTAS PARA FUNCIONAR COMO UM "BANCO DE DADOS" ONDE O GERADOR DE SENHA VAI PASSAR A ADOTAR COMO BASE PARA CRIAR AS SENHAS.
# ==================================================================================================================================================================== #

import string
import random

# listNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# listSpecialCarachter = ['!', '€', '$', '%', '&', '?', '§', '=']
# listAlfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

characters = list(string.ascii_letters + string.digits + "!@#$%&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    password = "".join(password)
    
    print(password)

option = input("Do you want to generate a password? (Yes / No)? ")

if option == "Yes":
    generate_password()
elif option == "No":
    print("Program Ended")
    quit()
else: 
    print("Invalid input, please Yes or No ")
    quit()