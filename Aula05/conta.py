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