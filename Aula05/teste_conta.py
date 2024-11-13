from conta import Conta

def criar_conta() -> None:
    conta = Conta('21.342-7')
    conta.creditar(500.87)
    conta.debitar(45.00)
    print("Conta número: {} - Saldo: {}".format(conta.get_numero(), conta.get_saldo()))

if __name__ == '__main__':
    criar_conta()