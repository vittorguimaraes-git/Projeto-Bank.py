def login_user():
    global usuarios
    global user_on
    global admin

    """
    Função para realizar o login do usuário.
    """
    print("Login".center(50))
    print("-"*50)
    print()

    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")

    # Aqui você pode adicionar a lógica para verificar o login do usuário
    # Por exemplo, você pode comparar com um banco de dados ou uma lista de usuários

    if username == "admin" and password == "admin":
        print("Login bem-sucedido!")
        admin = True
        return admin
    
    elif username in usuarios and usuarios[username] == password:
        print("Login bem-sucedido!")
        user_on = True
        return user_on
    else:
        print("Nome de usuário ou senha incorretos.")
        return False

if __name__ == "__main__":
    login_user()
    