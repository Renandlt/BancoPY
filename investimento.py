# IMPORTAÇÕES
import os
from time import sleep

# VALIDAÇÃO DE INVESTIMENTO
def investir(valor, saldo, i, valorM, valorIn, imoeda, moedas):
    # ESTRUTURA DE CONDICIÇÃO
    if valor > saldo[i]:
        print("Saldo insuficiente")
    elif valor <= saldo[i]:
        print(
            f"\nR${valor}, você pode comprar {valor/valorM[imoeda]:.2f} moedas de {moedas[imoeda]}.\nDeseja continuar com a transação?"
        )
        x = input('Digite [Y] para "Sim" ou [N] para "Não":').lower()
        if x == "y":
            saldo[i] -= valor
            print(
                f"R${valor} foi investido da sua conta, seu novo saldo é R${saldo[i]}"
            )
            valorIn[i][imoeda] += valor  
            print(f"Você tem R${valorIn[i][imoeda]:.2f} na {moedas[imoeda]}")

        elif x == "n":
            print("Ação cancelada")

# FUNÇÃO DE CALCULO E CONFIRMAÇÃO
def retirar(valor, imoeda, valorIn, saldo, i, moedas):
    # ESTRUTURA DE CONDICIÇÃO
    if valor > valorIn[i][imoeda]:  
        print("Saldo insuficiente")
    elif valor <= valorIn[i][imoeda]:  
        print(
            f"\nSera retirado R${valor} da moeda, você terá R${valorIn[i][imoeda] - valor} restantes.\nDeseja continuar com a transação?"
        )
        x = input('Digite [Y] para "Sim" ou [N] para "Não":').lower()
        os.system('cls')
        if x == "y":
            saldo[i] += valor
            print(f"R${valor} foi retirado, seu novo saldo é R${saldo[i]}")
            valorIn[i][imoeda] -= valor  
            print(f"Você tem R${valorIn[i][imoeda]:.2f} na {moedas[imoeda]}")


def mmoeda(imoeda, moedas, valorM, valorIn, saldo, i):
    print("--------------------\n---Mercado Cripto---\n--------------------\n")
    print(f"{moedas[imoeda]} - R${valorM[imoeda]}\n")

    print("Selecione um valor para investir:")
    print("[1] - 200 R$\n[2] - 500 R$ \n[3] - 1000 R$\n[0] - Voltar\n")
    print("Digite qualquer outro valor caso necessário.")

    valor = float(input("Digite o valor que deseja investir (ou 0 para sair): "))
    os.system('cls')
    # ESTRUTURA DE CONDICIÇÃO
    if valor == 0:
        print("Saindo...")
        sleep(2)
        return

    if valor != 1 and valor != 2 and valor != 3 and valor != 0:
        os.system('cls')
        investir(valor, saldo, i, valorM, valorIn, imoeda, moedas)

    if valor == 1:
        os.system('cls')
        investir(200, saldo, i, valorM, valorIn, imoeda, moedas)

    if valor == 2:
        os.system('cls')
        investir(500, saldo, i, valorM, valorIn, imoeda, moedas)

    if valor == 3:
        os.system('cls')
        investir(1000, saldo, i, valorM, valorIn, imoeda, moedas)


def rmoeda(imoeda, moedas, valorM, valorIn, saldo, i):
    print("--------------------\n---Mercado Cripto---\n--------------------\n")
    print(
        f"{moedas[imoeda]} - Moedas: {valorIn[i][imoeda] / valorM[imoeda]:.2f} - Total: R${valorIn[i][imoeda]:.2f}\n"
    )

    print("Selecione um valor para retirar:")
    print("[1] - 200 R$\n[2] - 500 R$ \n[3] - 1000 R$\n[0] - Voltar\n")
    print("Digite qualquer outro valor caso necessário.")

    valor = float(input("Digite o valor que deseja retirar (ou 0 para sair): "))
    os.system('cls')

    if valor == 0:
        print("Saindo...")
        return

    if valor != 1 and valor != 2 and valor != 3 and valor != 0:
        retirar(valor, imoeda, valorIn, saldo, i, moedas)
        sleep(2)
        os.system('cls')
    if valor == 1:
        retirar(200, imoeda, valorIn, saldo, i, moedas)
        sleep(2)
        os.system('cls')
    if valor == 2:
        retirar(500, imoeda, valorIn, saldo, i, moedas)
        sleep(2)
        os.system('cls')
    if valor == 3:
        retirar(1000, imoeda, valorIn, saldo, i, moedas)
        sleep(2)
        os.system('cls')

# MERCADO DE INVESTIMENTO
def mcripto(saldo, i, moedas, valorM, valorIn, sorte):
    # ESTRUTURA DE REPETIÇÃO
    while True:
        y = 0
        print("--------------------\n---Mercado Cripto---\n--------------------\n")

        print(f"Seu saldo é R${saldo[i]}\nMoedas:")

        for _ in range(len(moedas)):
            if sorte[y] < 0:
                c = "↓"
            elif sorte[y] > 0:
                c = "↑"

            print(f"[{y+1}] - {moedas[y]} - R${valorM[y]:.2f} {c}")
            y += 1

        print("[0] - Voltar")
        x = int(input("Selecione uma moeda:"))
        os.system('cls')
        
        if x != 0 and x >= 1 and x <= len(moedas):
            x -= 1
            mmoeda(x, moedas, valorM, valorIn, saldo, i)
            sleep(2)
            os.system('cls')
        elif x == 0:
            break
        else:
            print("Opção inválida.\n")
            sleep(2)
            os.system('cls')

# MENU MOEDAS INVESTIDAS
def minhasmoedas(moedas, valorM, valorIn, saldo, i):
    y = 0
    print("---------------------\n-----Suas Moedas-----\n---------------------\n")
    for _ in range(len(moedas)):
        print(
            f"{y + 1}. {moedas[y]} - R${valorM[y]:.2f} - Moedas: {valorIn[i][y] / valorM[y]:.2f} - Total: R${valorIn[i][y]:.2f}"
        )
        y += 1
    print("\n[0] - Voltar")

    x = int(input("Selecione uma moeda:"))
    os.system('cls')

    if x != 0 and x >= 1 and x <= len(moedas):
        x -= 1
        os.system('cls')
        rmoeda(x, moedas, valorM, valorIn, saldo, i)

    elif x == 0:
        pass
    else:
        print("Opção inválida.\n")
        sleep(2)
        os.system('cls')

# MENU DE INVESTIMENTOS
def minvest(saldo, i, moedas, valorM, valorIn, sorte):
    while True:
        print("--------------------\n---Mercado Cripto---\n--------------------\n")
        print("[1] - Investir em moedas\n[2] - Moedas investidas")
        print("[0] - Voltar")

        opcao = input("\nSelecione uma opção:")
        os.system('cls')
        
        if opcao == "1":
            os.system('cls')
            mcripto(saldo, i, moedas, valorM, valorIn, sorte)
        elif opcao == "2":
            os.system('cls')
            minhasmoedas(moedas, valorM, valorIn, saldo, i)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
            sleep(2)
            os.system('cls')
