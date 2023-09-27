# IMPORTAÇÕES
from conta import conta
from emprestimo import menuEmp
from transferencia import mtranfsel
from suporte import suporte
from investimento import minvest
from time import sleep
import os

# MENU PRINCIPAL
def menu(i,saldo,fatura,valorM,sorte,v,renda,contas,moedas,valorIn):
    # ESTRUTURA DE REPETIÇÃO
    while True:
        print("------------------\n--Menu Principal--\n------------------\n")
        print(
            "[1] - Conta\n[2] - Emprestimo \n[3] - Transferencia\n[4] - Investimentos \n[5] - Suporte \n[0] - Sair\n"
        )

        x = int(input("Digite um numero:"))
        # ESTRUTURA DE CONDIÇÃO
        if x == 1:
            os.system('cls')
            print("[Conta] Selecionada")
            sleep(2)
            os.system('cls')
            conta(saldo, i, fatura, valorM, sorte, v)
            
        elif x == 2:
            os.system('cls')
            print("[Emprestimo] Selecionado")
            sleep(2)
            os.system('cls')
            menuEmp(saldo, i, fatura, renda)

        elif x == 3:
            os.system('cls')
            print("[Transferencia] Selecionado")
            sleep(2)
            os.system('cls')
            mtranfsel(contas, saldo, i)

        elif x == 4:
            os.system('cls')
            minvest(saldo, i, moedas, valorM, valorIn, sorte)

        elif x == 5:
            os.system('cls')
            suporte()
            
        elif x == 0:
            print("Saindo...\n")
            break
        else:
            print("Opção Invalida")
