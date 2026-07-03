from time import sleep
from menu import menu_banco
from login import login_user
from header import header_bank

linha = ("-"*50)
usuarios = {}
user_on = False
admin = False

while True:

    # Corpo do programa

    header_bank()
    menu_banco()
    print()

    try:
        opcao = int(input("INFO| Escolha uma opção: "))
        print()


        if opcao == 1:

            login_user()

            while user_on:

                print()
                print(linha)
                print(f'Bem-Vindo, {username.title()}'.center(50))
                print(linha)
                print()

                        # Futura menu de usuário logado
                    

                opcao = int(input('INFO|Escolha uma opção: '))
                print(linha)

                if opcao == 1:
                    print()

                # Lógica futura

                elif opcao == 2:
                    print()

                # Lógica futura

                elif opcao == 3:


                    print()
                    print(linha)
                    print("Saindo da sua conta...")
                    print(linha)
                    print()
                    sleep(1)
                    user_on = False


        elif opcao == 2:

            print(linha)
            print("Cadastro".center(50))
            print(linha)
            print()

            username = input('Username: ')
            password = input('Password: ')
            print()

            if username in usuarios:
                print(linha)
                print('ERRO|Usuário já cadastrado!')
                print(linha)
                print()
            else:
                usuarios[username] = password
                print(linha)
                print('INFO|Usuário cadastrado!')
                print(linha)
                print()


                # lógica futura aqui

        elif opcao == 3:

            print(linha)
            print()
            print("Saindo...")
            print()
        
            sleep(1)
            print(linha)
            print('Obrigado por utilizar!')
            break

        else:
            print()
            print(linha)
            print('ERRO| Escolha uma opção válida!')
            print(linha)


    except ValueError:
        print()
        print(linha)
        print('ERRO| Escolha uma opção válida!')
        print(linha)
