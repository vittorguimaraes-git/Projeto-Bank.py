from src.headers import header_bank, header_login, header_register
from src.menu import menu_bank
from  time import sleep

dados = dict()
linha = "-"*50


while True:

    header_bank()
    print()

    menu_bank()
    print()

    option = input(f"Digite a opção desejada: (Ex: 1) ")
    print()
    
    if option == "1":
        from src.login import login
        
        header_login()
        login(username=input("Username: "), password=input("Password: "), dados=dados)
        print()
        
    elif option == "2":
        from src.register import register
        header_register()
        register(dados)

    elif option == "0":
        print(f"\n{'-'*50}\n[INFO] - Saindo do sistema...\n{'-'*50}")
        sleep(1.5)
        break

    else:
        print(f"\n{'-'*50}\n[ERRO] - Opção inválida! Tente novamente.\n{'-'*50}")
        sleep(1.5)