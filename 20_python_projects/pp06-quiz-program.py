# ==================================================================================================================================================================== #
# CREATE A DICTIONARY THAT STORES QUESTIONS AND ANSWERS
# HAVE A VARIABLE THAT TRACKS THE SCORE OF THE PLAYER
# LOOP THROUGH THE DICTIONARY USING THE KEY VALUES PAIRS
# DISPLAY EACH QUESTION TO THE USER AND ALLOW THEM TO ANSWER
# TELL THEM IF THEY ARE RIGHT OR WRONG 
# SHOW THE FINAL RESULT WHEN QUIZ IS COMPLETED
# ==================================================================================================================================================================== #

quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlim"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Berna"
    },
    "question7": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    },
}

# ==================================================================================================================================================================== #
# ESSE DICIONARIO FAZ O VALUE "questionX" VALER DOIS VALORES "question" E "answer" NA SEQUENCIA
# ==================================================================================================================================================================== #

score = 0 

# ==================================================================================================================================================================== #
# UM LAçO FOR PARA PASSAR DENTRO DE CADA UMA DAS QUESTOES DE CIMA, UMA A UMA, NAO SORTEANDO MAS DIZENDO UMA A UMA.
# DEPOIS VAI IMPRIMIR A QUESTAO E VAI FAZER A PERGUNTA PARA QUE O USUARIO FAçA O INPUT DA RESPOSTA. 
# DEPOIS DISSE SE INICIA UM LAçO "if" PARA CONFERIR A RESPOSTA INSERIDA PELO USUARIO CONTRA A RESPOSTA PROGRAMADA DENTRO DA APLICACAO, INSERIDA NO DICIONARIO ANTES.
# SE A "answer" FOR IGUAL A ANTERIORMENTE REGISTRADA, VAI ESCREVER CORRETO E CONTAR O PONTO. CASO CONTRARIO ERRADO, APRESENTAR A RESPOSTA E NAO SOMAR PONTO ALGUM. 
# ESSE LAçO "if" TEM QUE SER DENTRO DO LAçO "for" DO DICIONARIO PARA FUNCIONAR PARA CADA UMA DAS RESPOSTAS.
# ==================================================================================================================================================================== #

for key, value in quiz.items(): 
    print(value['question']) 
    answer = input("Answer? ") # SERIA MELHOR CHAMAR DE "clientAnswer" MAS VOU MANTER A VARIAVEL ASSIM PARA SEGUIR O TUTORIAL
    
    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print('Your score is: ' + str(score))
        
    else:
        print("Wrong!")
        print("The answer is " + value['answer'])
        print("Your score is " + str(score))
        print("")

print("You got " + str(score) + "out of 7 questions correctly")
print("Your percentage is " + str(int(score/7 * 100)) + "%")