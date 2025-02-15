# Fomos contratados por um grande banco para desenvolver
# o seu novo sistema. Esse banco deseja modernizar
# suas operações e para isso escolheu a linguagem Python.
# Para a primeira versão do sistema devemos implementar
# apenas 3 operações: depósito, saque e extrato.

# DEPÓSITO
# Deve ser possível depositar valores positivos 
# para a minha conta bancária. A v1 do projeto trabalha 
# apenas com 1 usuário, dessa forma não precisamos nos 
# preocupar em identificar qual é o número da agência e
# conta bancária. Todos os depósitos devem ser armazenados 
# em uma variável e exibidos na operação de extrato.

# SAQUE
# O sistema deve permitir realizar 3 saques diários com 
# limite máximo de R$ 500,00 por saque. Caso o usuário não 
# tenha saldo em conta, o sistema deve exibir uma mensagem
# informando que não será possível sacar o dinheiro por
# falta de saldo. Todos os saques devem ser armazenados em 
# uma variável e exibidos na operação de extrato.

# EXTRATO
# Essa operação deve listar todos os depósitos e saques
# realizados na conta. No fim da listagem deve ser exibido 
# o saldo atual da conta.
# Os valores devem ser exibidos utilizando o formato R$ xxx.xx
# Exemplo:
# 1500,45 = R$ 1500.45

saldo = 0
quantidade_saques_de_hoje = 0
QUANTIDADE_MAXIMA_DE_SAQUES = 3

extrato = f"""
=========================================
===              EXTRATO              ===
=========================================

"""

menu = """
=========================================
===               MENU                ===
=========================================

[1] = Depósito
[2] = Saque
[3] = Extrato
[0] = Sair

"""
def deposito(valor):
    global extrato
    global saldo

    if valor > 0:
        extrato += f"\n DEPÓSITO: R$ {valor}"
        saldo += valor

        print("Valor depositado com sucesso!")
    else:
        print("Para depositar você deve digitar um valor positivo")

def saque(valor):
    global quantidade_saques_de_hoje
    global extrato
    global saldo
    global QUANTIDADE_MAXIMA_DE_SAQUES

    if valor > 0:
        if valor < saldo:
            if quantidade_saques_de_hoje < QUANTIDADE_MAXIMA_DE_SAQUES:
                if valor > 500:
                    print("O valor máximo para saque é de R$ 500.00")
                else:
                    extrato += f"\n SAQUE: R$ {valor}"
                    saldo -= valor
                    quantidade_saques_de_hoje += 1

                    print("Valor sacado com sucesso!")
            else:
                print("Voce atingiu a quantidade máxima de saques diários")
        else:
            print("Para sacar você precisa ter o valor em sua conta! Verifique seu extrato")
    else:
        print("Para Sacar você precisa digitar um valor positivo!")

while True:
    opcao = int(input(menu))
    
    if opcao == 0:
        print('Obrigado por utilizar nosso banco!')
        print()

        break
    
    elif opcao == 1:
        valor_deposito = float(input("Digite o valor do depósito: "))

        deposito(valor_deposito)

        print(f'Saldo: R$ {saldo}')
    
    elif opcao == 2:
        valor_saque = float(input("Digite o valor a sacar: "))

        saque(valor_saque)

        print(f'Saldo: R$ {saldo}')

    elif opcao == 3:
        print(extrato)
        print()
        print(f'SALDO: {saldo}')
    
    else:
        print("Digite uma opção válida!")
        print()
        print(f'SALDO: {saldo}')
