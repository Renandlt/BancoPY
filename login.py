# IMPORTAÇÕES
from menu import menu
from time import sleep
import os

# FUNÇÃO DE INDICE
def ind(y, lista):
    for i in range(len(lista)):
        if lista[i] == y:
            return i
    return -1

# CADASTRO
def signup(contas,senhas,saldo,fatura,valorM,sorte,v,renda,moedas,valorIn):
    # ESTRUTURA DE REPETIÇÃO
    while True:
        print("---------------------\n--------Entrar-------\n---------------------\n")
        print("Informe seus dados de login.\nDigite [0] para sair")

        x = input("Digite seu nome:")

        if x == "0":
            break

        # Verificar se x está na lista de contas, mudar o índice para a posição da conta
        if x.lower() in contas:
            i = ind(x, contas)
            x = input("Digite sua senha:")
            # Verificar se a conta existe
            if x == senhas[i]:
                print(f"Seja bem-vindo {contas[i]}")
                sleep(2)
                os.system('cls')
                menu(i, saldo, fatura, valorM, sorte, v, renda, contas, moedas, valorIn)
            else:
                print("Senha Incorreta")
                sleep(2)
                os.system('cls')
        else:
            print("Login Incorreto")
            sleep(2)
            os.system('cls')

# CRIAR CONTA            
def CriarConta(contas,senhas,saldo,fatura,renda,valorIn):
    x = input("Digite o nome de usuário:")

    if x in contas:
        print("Usuário já está em uso.")
    else:
        y = input("Digite a senha:")
        z = input("Digite a senha novamente:")
        if y == z:
            c = float(input("Digite sua renda:"))

            contas.append(x.lower())
            senhas.append(y)
            saldo.append(1000)
            renda.append(c)
            fatura.append(0)
            valorIn.append([0, 0, 0])

            print("Sua conta foi criada com sucesso\nVocê recebeu R$1000 por ter criado uma conta.")
            sleep(2)
            os.system('cls')
        else:
            print("Senha incorreta")

# MENU DE LOGIN/CADASTRO
def banco(contas,senhas,saldo,fatura,valorM,sorte,v,renda,moedas,valorIn):
    while True:
        print("--------------------\n------Banco PY------\n--------------------\n")
        print(
            "[1] - Entrar\n[2] - Criar Conta\n[0] - Sair\n"
        )
        
        x = input("Selecione uma opção:")
        os.system('cls')
        if x == "0":
            print("Saindo...")
            break
        elif x == "1":
            signup(contas,senhas,saldo,fatura,valorM,sorte,v,renda,moedas,valorIn)
        elif x == "2":
            CriarConta(contas,senhas,saldo,fatura,renda,valorIn)
        else:
            print("Opção inválida. Tente novamente.")


