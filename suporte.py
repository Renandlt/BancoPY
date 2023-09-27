# IMPORTAÇÕES
from time import sleep
import os

# Função com as principais duvidas de nosso clientes; 
# Argumentos da função é somente para voltar para o menu principal como o usuario;
def suporte():
    # ESTRUTURA DE REPETIÇÃO
    while True:
        print("--------------------\n---Menu de Suporte---\n--------------------\n")
        print(
            "[1] - Como verificar seu saldo\n"
            "[2] - Como pagar sua fatura\n"
            "[3] - Como investir em moedas criptografadas\n"
            "[4] - Como solicitar um empréstimo\n"
            "[5] - Como fazer uma transferência\n"
            "[6] - Como verificar seu extrato\n"
            "[7] - Como esperar para atualizar os valores de moedas criptografadas\n"
            "[0] - Voltar\n"
        )

        x = int(input("Digite o número da opção que você deseja obter ajuda: "))

        # ESTRUTURA CONDICIONAL
        if x == 0:
            os.system('cls')
            print("Saindo do menu de suporte...")
            sleep(3)
            os.system('cls')
            return

        elif x == 1:
            os.system('cls')
            print("Para verificar seu saldo, selecione a opção 'Conta' no menu principal.")
            sleep(3)
            os.system('cls')
            

        elif x == 2:
            print("Para pagar sua fatura, selecione a opção 'Conta' no menu principal e escolha 'Pagar Fatura'.")
            sleep(3)
            os.system('cls')
            

        elif x == 3:
            print("Para investir em moedas criptografadas, selecione a opção 'Investimentos' no menu principal.")
            sleep(3)
            os.system('cls')
            

        elif x == 4:
            print("Para solicitar um empréstimo, selecione a opção 'Empréstimo' no menu principal.")
            sleep(3)
            os.system('cls')
            

        elif x == 5:
            print("Para fazer uma transferência, selecione a opção 'Transferência' no menu principal.")
            sleep(3)
            os.system('cls')
            

        elif x == 6:
            print("Atualmente, a opção de verificação de extrato não está disponível.")
            sleep(3)
            os.system('cls')
            

        elif x == 7:
            print("A opção 'Esperar' permite atualizar os valores de moedas criptografadas, mas o detalhe exato do processo não está especificado.")
            sleep(3)
            os.system('cls')
            

        else:
            print("Opção inválida. Tente novamente.")
            sleep(3)
            os.system('cls')
