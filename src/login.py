def login(username, password, dados):

    if username in dados and dados[username]["senha"] == password:
        print(f"\n{'-'*50}\n[INFO] - Login realizado com sucesso!\n{'-'*50}")
        return True
    else:
        print(f"\n{'-'*50}\n[ERRO] - Usuário ou senha incorretos!\n{'-'*50}")
        return False
