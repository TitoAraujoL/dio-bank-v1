"""
    Projeto - Sistema bancário - DIO - V1

Exigências:

- Apenas 1 usuário
- Todos os depósitos devem ser armazenados em uma variável e exibido na variável extrato
- O sistema deve permitir 3 saques diários com limite de R$ 500,00
- Não será possível sacar sem saldo
"""

import datetime

menu = """
    Sistema Bancário  - DIO

 [1] - Depositar
 [2] - Sacar
 [3] - Extrato
 [4] - Saldo
 [5] - Sair
"""

saldo = 0.0
limite_de_saque = 3
saques_diarios = 0
extrato = []
contador = 0


def depositar(valor):
    global saldo
    global extrato

    saldo += valor
    data_criacao = datetime.datetime.now()

    extrato.append({"descricao": "Depósito", "valor": valor, "data": data_criacao})

    print(f"\nDepositado R$ {valor:.2f} na sua conta")


def sacar(valor):
    global saldo
    global extrato

    if valor > 0 and valor <= saldo:
        saldo -= valor
        data_criacao = datetime.datetime.now()

        print(f"\nSaque de R$ {valor:.2f} foi realizado com sucesso.\n")

        extrato.append({"descricao": "Saque", "valor": valor, "data": data_criacao})
    else:
        print("\nSaldo insuficiente\n")


def mostrar_extrato():
    global extrato

    print("\nExtrato:\n")
    for item in extrato:
        descricao = item.get("descricao", "").center(10)
        valor = item.get("valor", 0.0)
        print(f" {descricao} ------------------------------ R$ {valor:.2f} ")


def mostrar_saldo():
    global saldo
    print(f"\nSaldo em conta: R$ {saldo:.2f}\n")


while True:
    print(menu)
    try:
        opcao = int(input("Selecione uma opção: "))
    except ValueError:
        print("Opção inválida. Digite um número.")
        continue

    match opcao:
        case 1:
            valor = float(input("Informe o valor de depósito: "))
            depositar(valor)
        case 2:
            valor = float(input("Informe o valor de saque: "))
            sacar(valor)
        case 3:
            mostrar_extrato()
        case 4:
            mostrar_saldo()
        case 5:
            print("Saindo...")
            break
        case _:
            print("Opção inválida.")
