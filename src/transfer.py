def transfer(dados, username):

    while True:
        try:
            valor = float(input(f"Digite o valor a ser transferido: R$ "))
            if valor <= 0:
                print(f"\n{'-'*50}\n[ERRO] - Valor inválido! Tente novamente.\n{'-'*50}")
                continue
            break
        except ValueError:
            print(f"\n{'-'*50}\n[ERRO] - Valor inválido! Tente novamente.\n{'-'*50}")

    while True:
        conta_destino = input(f"Digite a conta de destino: ")
        if conta_destino not in dados:
            print(f"\n{'-'*50}\n[ERRO] - Conta de destino não encontrada! Tente novamente.\n{'-'*50}")
            continue
        break

    if dados[username]["saldo"] < valor:
        print(f"\n{'-'*50}\n[ERRO] - Saldo insuficiente para realizar a transferência!\n{'-'*50}")
        return

    dados[username]["saldo"] -= valor
    dados[conta_destino]["saldo"] += valor

    print(f"\n{'-'*50}\n[INFO] - Transferência realizada com sucesso!\n{'-'*50}")