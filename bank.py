from src.header import header
from src.menu import menu_bank, menu_user
from  time import sleep

dados = dict()
linha = "-"*50
user_on = False

while True:

    header("Bem vindo ao Banco Python")
    print()

    menu_bank()
    print()

    option = input(f"Digite a opção desejada: (Ex: 1) ")
    print()
    
    if option == "1":
        from src.login import login
        
        header("Login")
        login(username=input("Username: "), password=input("Password: "), dados=dados)
        print()

    elif option == "2":
        from src.register import register
        header("Cadastro de Usuário")
        register(dados)

    elif option == "0":
        print(f"\n{'-'*50}\n[INFO] - Saindo do sistema...\n{'-'*50}")
        sleep(1.5)
        break

    else:
        print(f"\n{'-'*50}\n[ERRO] - Opção inválida! Tente novamente.\n{'-'*50}")
        sleep(1.5)