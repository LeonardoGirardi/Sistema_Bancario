saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def menu():
    while True:
        print("""
              (1) Depósito
              (2) Saque
              (3) Extrato
              (0) Sair
              """)

        try:
            opcao = int(input("Selecione a Opção: "))
            if opcao in [0, 1, 2, 3]:
                return opcao
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")


def deposito():
    global saldo, extrato

    print("Função de Depósito")

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")


def saque():
    global saldo, limite, extrato, numero_saques
    print("___________Função de Saque____________")

    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")


def extrato_func():
    global extrato, saldo
    print("_______________Função de Extrato________________")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def sistema():
    while True:
        opcao = menu()

        if opcao == 1:
            deposito()

        elif opcao == 2:
            saque()

        elif opcao == 3:
            extrato_func()

        elif opcao == 0:
            print("Saindo...")
            break


sistema()
