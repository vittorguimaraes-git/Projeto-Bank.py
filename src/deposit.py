def deposit(dados, username):
   
    while True:
        try:
            valor = float(input("Valor: "))

            if valor <= 0:

                print(f"\n{'-'*50}\n[ERRO] - Valor inválido! Tente novamente.\n{'-'*50}")
                continue

            if valor > 0:

                print(f"\n{'-'*50}\n[INFO] - Valor depositado com sucesso! \n{'-'*50}")
                dados[username]["saldo"] += valor

            break
        except ValueError:
            print(f"\n{'-'*50}\n[ERRO] - Valor inválido! Tente novamente.\n{'-'*50}")
  
        
