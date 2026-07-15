def login(username, password, dados):

    global user_on

    if username in dados and dados[username]["senha"] == password:
        print(f"\n{'-'*50}\n[INFO] - Login realizado com sucesso!\n{'-'*50}")
        user_on = True
        
    else:
        print(f"\n{'-'*50}\n[ERRO] - Usuário ou senha incorretos!\n{'-'*50}")
        return False

    if user_on:
        from src.header import header
        from src.menu import menu_user
        from time import sleep

        while True:
            header(f"Bem vindo, {username.title()}!")
            menu_user()
            print()
                
            option_user = input(f"Digite a opção desejada: (Ex: 1) ")
            print()
                
            if option_user == "1":
                from src.consult import consult
                header("Consultar Saldo")
                consult(dados, username)
                sleep(1.5)
                
            elif option_user == "2":
                from src.transfer import transfer
                header("Transferir")
                transfer(dados, username)
                sleep(1.5)
                
            elif option_user == "3":
                from src.deposit import deposit
                header("Depositar")
                deposit(dados, username)
                sleep(1.5)
                
            elif option_user == "0":
                user_on = False
                sleep(1.5)
                break
                
            else:
                print(f"\n{'-'*50}\n[ERRO] - Opção inválida! Tente novamente.\n{'-'*50}")
                sleep(1.5)