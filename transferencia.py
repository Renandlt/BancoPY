# IMPORTAÇÕES
from time import sleep
import os

# Função de transferir dinheiro para usuario
def transf(valor, saldo, contas, conta1, conta2):
    # ESTRUTURA CODICIONAL
    if saldo[conta1] >= valor:
        saldo[conta1] = saldo[conta1] - valor
        print(f"{valor} foi retirado da sua conta, seu novo saldo é {saldo[conta1]}")
        saldo[conta2] = saldo[conta2] + valor
        sleep(2)
        os.system('cls')
        
        
    else:
        print('Você não possui saldo suficiente!')
        sleep(2)
        os.system('cls')

# Função do menu de transferencia        
def mtranf(contas, conta2, saldo, conta1):
    print(
            "-----------------------\n-Menu de Transferencia-\n-----------------------\n"
        )
    print("[1] - 200 R$\n[2] - 500 R$ \n[3] - 1000 R$\n[0] - Voltar\n")
    print("Digite qualquer outro valor caso necessario.")

    valor = int(input("Digite o valor que deseja transferir (ou 0 para sair): "))
    # ESTRUTURA CONDICIONAL
    if valor != 1 and valor != 2 and valor != 3 and valor != 0:
        transf(valor, saldo, contas, conta1, conta2)
        sleep(2)
        os.system('cls')
    if valor == 1:
        transf(200, saldo, contas, conta1, conta2)
        sleep(2)
        os.system('cls')
    if valor == 2:
        transf(500, saldo, contas, conta1, conta2)
        sleep(2)
        os.system('cls')
    if valor == 3:
        transf(1000, saldo, contas, conta1, conta2)
        sleep(2)
        os.system('cls')
    if valor == 0:
        os.system('cls')
        return
        


def mtranfsel(contas, saldo, i):
    # ESTRUTURA DE REPETIÇÃO
    while True:
        y = 0

        print(
            "-----------------------\n-Menu de Transferencia-\n-----------------------\n"
        )
        print(f"Possiveis Transferencias:")

        for z in range(len(contas)):
            print(f"[{y+1}] - {contas[y]}")
            y += 1

        print("[0] - Voltar")
        x = int(input("Digite o usuario que voce deseja transferir:"))

        # ESTRUTURA DE CONDIÇÃO
        if x != 0 and x >= 1 and x <= len(contas):
            x -= 1
            mtranf(contas, x, saldo, i)

        elif x == 0:
            os.system('cls')
            break
        else:
            os.system('cls')
            print("Opção inválida.\n")
