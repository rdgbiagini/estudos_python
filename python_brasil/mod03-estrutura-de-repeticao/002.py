""" Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. """

login = str(input('CRIE LOGIN: '))
senha = str(input('CRIE SENHA: '))
while login == senha:
    print('ERRO. Não podem ser a mesma informação. ')
    login = str(input('CRIE LOGIN: '))
    senha = str(input('CRIE SENHA: '))
else:
    print('CADASTRO EFETUADO COM SUCESSO. ')
