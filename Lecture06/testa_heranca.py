from heranca import Conta, ContaPoupanca

def teste():
    tipo_conta = input("Digite se vai ser conta corrente (1) ou poupança (2)")
    if tipo_conta == '1':
        conta = Conta('125')
    else:
        conta = ContaPoupanca('125')
    conta.creditar(1000)
    if isinstance(conta, ContaPoupanca):
        conta.render_juros(0.01)
    print("O saldo da conta é: {}".format(conta.get_saldo()))

if __name__ == '__main__':
    teste()