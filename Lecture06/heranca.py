class Conta:

    def __init__(self, numero:str):
        self.__numero = numero
        self.__saldo = 0.0

    def creditar(self, valor:float) -> None:
        self.__saldo += valor

    def debitar(self, valor:float) -> None:
        self.__saldo -= valor

    def get_numero(self) -> str:
        return self.__numero

    def get_saldo(self) -> float:
        return self.__saldo
    
class ContaPoupanca(Conta):

    def __init__(self, numero:str):
        super().__init__(numero)

    def render_juros(self, taxa: float) -> None:
        self.creditar(self.get_saldo() * taxa)

class ContaEspecial(Conta):

    def __init__(self, numero:str):
        super().__init__(numero)

    def render_bonus(self) -> None:
        super().creditar(self.__bonus)
        self.__bonus = 0

    # Polimorfismo de método
    def creditar(self, valor:float) -> None:
        self.__bonus += valor * 0.01
        super().creditar(valor)