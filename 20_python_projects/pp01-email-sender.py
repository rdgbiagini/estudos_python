# ==================================================================================================================================================================== #
# ESTUDO DE PYTHON - 20 PYTHON PROJECTS FOR BEGGINERS
# Link: https://www.youtube.com/watch?v=pdy3nh1tn6I
# PROJECT # 01 = E-mail sender
# ==================================================================================================================================================================== #

# ==================================================================================================================================================================== #
# GO TO OUT GMAIL ACOUNT (CREATE AN ACOUNT FOR THIS KIND OF TESTS) AND SETUP 2 FACTOR AUTHENTICATION 
# GENERATE AN APP PASSWORD
# CREATE A FUNCTION TO SEND AN E-MAIL 
# PARA ISSO CRIEI UM EMAIL DO GOOGLE "rbp.estudos@gmail.com" COM A SENHA "Biagini1986"
# O E-MAIL DE RECUPERACAO DESSE E-MAIL E O "rdg.biagini@gmail.com" O MEU PESSOAL
# ==================================================================================================================================================================== #

# ==================================================================================================================================================================== #
# PARA ISSO VAMOS CONECTAR ESSA CONTA DO GOOGLE NO PYTHON, QUE GERA ESSE CODIGO NO SITE DO GOOGLE
# CODIGO: ychh wqve dpii uund
# INSTRUCAO DE USO DO PROPRIO GOOGLE: 
# ETAPA 01 - Acesse as configurações da sua Conta do Google no aplicativo ou dispositivo que você está tentando configurar. 
# ETAPA 02 - Substitua sua senha pela senha de 16 caracteres mostrada acima. 
# ETAPA 03 - Assim como sua senha normal, esta senha de app concede acesso total à sua Conta do Google. 
# ETAPA 04 - Não é necessário memorizá-la, por isso não a anote ou a compartilhe com outras pessoas.
# ==================================================================================================================================================================== #

from email.message import EmailMessage
import ssl
import smtplib

contEmail = 1
rangeTotal = 10

for email in range(1, (rangeTotal + 1)): # COLOQUEI NESSE FOR APENAS PARA ME DIVERTIR MESMO. NEM PRECISAVA

    email_sender = 'rbp.estudos@gmail.com' # E-MAIL CRIADO ESPECIFICAMENTE PARA ESTUDOS E TESTES. 
    email_password = 'ychh wqve dpii uund' # SENHA GERADA PELO GOOGLE PARA ACESSO DO PYTHON. COLOQUEI ESSA SENHA AO INVES DA MINHA E FUNCIONOU.

    email_receiver = 'mailto:beatrizdejesus.santana@gmail.com', 'r.biagini86@gmail.com' # AQUI PODE SER, UMA LISTA DE REMETENTES, ONDE NO TEXTO A GENTE PODE SUBSTITUIR O NOME PELA STRING PARA PERSONALIZAR

    subject = f"E-MAIL # {contEmail} / {rangeTotal}"

    body = """ 
    Teste de envio de e-mail com integraçao da conta do Gmail com senha gerada internamente para acesso pelo Python.  
    """
    
    # AQUI A GENTE VAI DEFINIR NA VARIAVEL "body" O VALOR OU TEXTO QUE SERA ESCRITO NO CORPO DO EMAIL, PARA SER REPASSADO. 

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        contEmail += 1