
def replace_word():

    # ================================================================================================================================================================ #
    # A "str" FAZ O USUARIO INSERIR A FRASE. NESSE CASO ESTA SAINDO UMA STRING PRONTA, MAS PODEMOS ALTERAR ISSO SEMPRE. 
    # A "wordToReplace" FAZ O USUARIO DIZER AS PALAVRAS QUE ELE QUER SUBSTITUIR DA FRASE INTEIRA. 
    # A "wordReplacement" FAZ O USUARIO DIZER QUAL A PALAVRA QUE ELE QUER QUE ENTAO SUBSTITUA A PALAVRA QUE ESTA SAINDO NA IMPRESSAO FUTURA DA STRING
    # ================================================================================================================================================================ #
    
    str = "Hi guys, i am tomi, and hi hi hi hi"
    wordToReplace = input("Enter the word to replace: ")
    wordReplacement = input("Enter the word replacement: ")
    print(str.replace(wordToReplace, wordReplacement))

replace_word() # ESSE COMANDO, AO FINAL DA DEFINICAO DE UMA FUNCAO E O COMANDO QUE "CHAMA" UMA FUNCAO, OU SEJA, QUE ACIONA ELA, ATIVA ELA. 