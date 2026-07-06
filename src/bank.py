from header import header_bank
from menu import menu_banco
from login import login_user
from cadastro import cadastro
from menu_user import menu_user
from exit_user import exit_user
from exit import saida
from time import sleep

linha = ("-"*50)
usuarios = {}
user_on = False




while True:

    # Corpo do programa

    header_bank()
    menu_banco()
    print()

    try:

        opcao = int(input("[INFO] Escolha uma opção: "))
        print()


        if opcao == 1:

            login_user()




            username = input("Username: ")
            password = input("Password: ")
            print()
            
                    
                
            if username in usuarios and usuarios[username] == password:
                print("[INFO] Login bem-sucedido!")
                user_on = True
            
            else:
                print("Nome de usuário ou senha incorretos.")
                    

            while user_on:

                print()
                print(linha)
                print(f'Bem-Vindo, {username.title()}'.center(50))
                print(linha)
                print()

                menu_user()
                    
                opcao = int(input('[INFO]Escolha uma opção: '))
                print()
                

                if opcao == 1:
                    print()

                # Lógica futura

                elif opcao == 2:
                    print()

                # Lógica futura

                elif opcao == 3:

                    exit_user()
                    user_on = False
                    sleep(2)
                    break


        elif opcao == 2:

            cadastro()

            username = input('Username: ')
            password = input('Password: ')
            print()



            if username in usuarios:
                print(linha)
                print('[ERRO] Usuário já cadastrado!')
                print(linha)
                print()
            else:
                usuarios[username] = password
                print(linha)
                print('[INFO] Usuário cadastrado!')
                print(linha)
                print()


                # lógica futura aqui

        elif opcao == 3:

            saida()
            sleep(1)
            break

        else:
            print()
            print(linha)
            print('[ERRO] Escolha uma opção válida!')
            print(linha)


    except ValueError:
        print()
        print(linha)
        print('[ERRO] Escolha uma opção válida!')
        print(linha)
