"""
    Projeto - Sistema bancário - DIO - V1

Exigências:

- Apenas 1 usuário
- Todos os depósitos devem ser armazenados em uma variável e exibido na variável extrato
- O sistema deve permitir 3 saques diários com limite de R$ 500,00
- Não será possível sacar sem saldo
"""

import datetime
from random import randint
import re


login = """
 [1] - Logar
 [2] - Cadastrar usuario
 [3] - Sair
"""

menu = """
    Sistema Bancário  - DIO

 [1] - Depositar
 [2] - Sacar
 [3] - Extrato
 [4] - Saldo
 [5] - Cadastrar conta
 [6] - Sair
"""

saldo = 0.0
limite_de_saque = 3
extrato = []
usuarios = []
saque_diario = 0


def existe_conta(cpf):
    global usuarios
      
    dados_usuario = [u for u in usuarios if u["cpf"] == cpf]
    
    if dados_usuario[0].get("conta") is False:
        return False
    
    return True
    
def cadastrar_usuario():
    
    cpf = str(input("Digite seu CPF: ").strip().replace(".", "").replace("-", ""))
    
    cpf_valido = re.search("^[0-9]{11}$",cpf)
    
    if not cpf_valido:
        print("\nCPF inválido.")
        return
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("\nUsuário já cadastrado.")
            return

    nome = str(input("\nDigite seu nome: ").strip())
    logradouro = str(input("Digite seu endereço residencial: ").strip())
    
    novo_usuario = {
        "nome": nome,
        "cpf": cpf,
        "logradouro": logradouro,
        "conta": False
    }
    
    usuarios.append(novo_usuario)
    
    print("\nUsuário criado com sucesso.")


def cadastrar_conta():
    global CPF 
    global usuarios

    if usuarios is not None:            
        for usuario in usuarios:
            if CPF == usuario["cpf"] and not usuario["conta"]:
                aleatorio = randint(0, 999)
                conta = int(f"{CPF[-4:]}{aleatorio}")
                usuario["conta"] = conta
                cpf_oculto = "*" * 8 + CPF[-3:]
                print(f"Criado a conta {conta} para {usuario["nome"]} - CPF: {cpf_oculto}")
            else:
                print("Conta já existente")
                return


def depositar():
    global CPF
    
    global saldo
    global extrato
   
    conta = existe_conta(CPF)
    if not conta:
        print("O usuário precisa possuir uma conta para depositar")
        return
    
    valor = float(input("Informe o valor de depósito: "))
    
    saldo += valor
    data_criacao = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    extrato.append({"descricao": "Depósito", "valor": valor, "data": data_criacao})

    print(f"\nDepositado R$ {valor:.2f} na sua conta")
    

def sacar(valor):
    global saldo
    global extrato
    
    global saque_diario
      
    if saque_diario == 3:
        print("\nLimite de 3 saques diarios atingindo")
        return
    

    if valor > 0 and valor <= saldo and valor <= 500:
        saldo -= valor
        data_criacao = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

        print(f"\nSaque de R$ {valor:.2f} foi realizado com sucesso.\n")

        extrato.append({"descricao": "Saque", "valor": valor, "data": data_criacao})
        
        saque_diario += 1
        
    elif valor > 500:
        print("\nLimite de valor de saque atingido ")
        
    else:
        print("\nSaldo insuficiente\n")


def mostrar_extrato():
    global extrato

    print("\nExtrato:\n")
    
    if not extrato:
        print("Não foram realizadas movimentações")
        
    for item in extrato:
        descricao = item.get("descricao", "").center(10)
        valor = item.get("valor", 0.0)
        data_da_operacao = item.get("data")
        
        print(f" {data_da_operacao} -  {descricao} ------------------------------ R$ {valor:.2f}")


def mostrar_saldo():
    global saldo
    print(f"\nSaldo em conta: R$ {saldo:.2f}\n")


while True:
    
    print(login)
    
    try:
        opcao = int(input("Selecione uma opção: "))
    except ValueError:
        print("Opção inválida. Digite um número.")
        continue
    
    if opcao == 1:
        cpf = str(input("Digite seu CPF: ").strip().replace(".", "").replace("-", ""))
  
        if cpf in [u["cpf"] for u in usuarios]:
            
            CPF = cpf
            
            while True:
                print(menu)
                opcao = int(input("Selecione uma opção: "))
                
                match opcao:
                    case 1:
                        depositar()
                    case 2:
                        valor = float(input("Informe o valor de saque: "))
                        sacar(valor)
                    case 3:
                        mostrar_extrato()
                    case 4:
                        mostrar_saldo()
                    case 5:
                        cadastrar_conta()
                    case 6:
                        print("Saindo...")
                        break
                    case _:
                        print("Opção inválida.")
        else:
            print("\nCPF não cadastrado, crie uma conta")
    
    elif opcao == 2:
        cadastrar_usuario()
        
    else:
        break
