from sisbanco import Banco, Conta

def terminal():

    sisbanco = Banco()

    while(True):

        print("SisBanco::Bem-Vindo!")
        print(".::Opcoes::.")
        print("[0]--CriarConta")
        print("[1]--Creditar")
        print("[2]--Debitar")
        print("[3]--Transferir")
        print("[4]--Saldo")
        print("[5]--Sair")
        opcao = int(input("Digite: "))

        if opcao == 0:
            numero = input("Digite o numero da conta: \n")
            conta = Conta(numero)
            sisbanco.cadastrar(conta)

        elif opcao == 1:
            numero = input("Digite o número da conta alvo: \n")
            valor = float(input("Digite o valor a ser creditado: \n"))
            sisbanco.creditar(numero, valor)

        elif opcao == 2:
            numero = input("Digite o número da conta alvo: \n")
            valor = float(input("Digite o valor a ser debitado: \n"))
            sisbanco.debitar(numero, valor)

        elif opcao == 3:
            origem = input("Digite o número da conta de origem: \n")
            destino = input("Digite o número da conta de destino: \n")
            valor = float(input("Digite o valor a ser transferido: \n"))
            sisbanco.transferir(origem, destino, valor)

        elif opcao == 4:
            numero = input("Digite o número da conta: ")
            print("O saldo da conta é: {}".format(sisbanco.saldo(numero)))

        elif opcao == 5:
            numero = input("Digite o número da conta alvo: \n")
            sisbanco.render_juros(numero)

        elif opcao == 6:
            numero = input("Digite o número da conta alvo: \n")
            sisbanco.render_bonus(numero)

        elif opcao == 7:
            numero = input("Digite a nova taxa: \n")
            sisbanco.set_taxa(numero)

        elif opcao == 8:
            print("SisBanco::Bye!")
            return


if __name__ == '__main__':
    terminal()