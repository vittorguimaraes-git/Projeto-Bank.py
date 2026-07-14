def register(dados):

    print("\n[INFO] - Username e password devem ter pelo menos\n         3 caracteres.\n")

    username = input("Username: ")
    passaword = input("Password: ")

    

    if username in dados:
        print(f"\n{'-'*50}\n[ERRO] - Usuário já cadastrado! Tente novamente.\n{'-'*50}")
        return
    elif len(username) < 3 or len(passaword) < 3:
        print(f"\n{'-'*50}\n[ERRO] - Nome de usuário e senha devem ter pelo menos 3 caracteres.\n{'-'*50}")
        return 
    else:
        dados[username] = {"senha": passaword, "saldo": 0.0}
        print(f"\n{'-'*50}\n[INFO] - Usuário cadastrado com sucesso!\n{'-'*50}")
