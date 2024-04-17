# ==================================================================================================================================================================== #
# 01 - COLLECT E-MAIL FROM USER
# SLICE / SPLIT THE E-MAIL USING THE "@" AS A POINT
# E-MAIL TESTE: hello@codewithtomi.com
# SET THE FIRST PART AS THE USERNAME AND THE SECOND PART AS THE DOMAIN
# SPLIT DOMAIN USING "."
# ==================================================================================================================================================================== #

def main():
    print("Welcome to the e-mail slicer! ")
    print("")
    
    email_input = input("Input your e-mail address: ").lower()
    
    username = email_input.split("@") # ESSA PARTE FAZ UM SPLIT PARA SEPARAR O ANTES DO @ COM O DEPOIS PARA SABER O QUE E USERNAME E O QUE E DOMAIN
    domain = email_input.split(".")
    extension = email_input.split(".") # ESSA PARTE PEGA O SPLIT JA FEITO E FAZ UM NOVO CONSIDERANDO UM SPLIT NO PONTO PARA JOGAR FORA E SABER SO DOMAIN
    
    print("username: ", username) 
    print("Domain: ", domain)
    print("Extension: ", extension)
    
main()