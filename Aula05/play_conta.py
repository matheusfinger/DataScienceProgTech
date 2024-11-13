from conta import Conta

def conteudo_conta() -> None:
    conta = Conta('21.342-7')
    conta.creditar(500.87)
    conta.debitar(45.00)
    print(dir(conta))

if __name__ == '__main__':
    conteudo_conta()