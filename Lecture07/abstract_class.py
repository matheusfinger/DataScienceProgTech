from abc import ABC, abstractmethod

class ContaAbstrata(ABC):
    
    def __init__(self, numero:str):
        self.__numero = numero
        self.__saldo = 0.0

    def creditar(self, valor:float) -> None:
        self.__saldo += valor

    @abstractmethod
    def debitar(self, valor:float) -> None:
        pass

    def get_numero(self) -> str:
        return self.__numero

    def get_saldo(self) -> float:
        return self.__saldo
    
class Conta(ContaAbstrata):
    def __init__(self, numero:str):
        super().__init__(numero)

    def debitar(self, valor:float) -> None:
        self.__saldo += valor

class ContaImposto(ContaAbstrata):
    def __init__(self, numero:str):
        super().__init__(numero)
        self.__taxa = 0.001
    
    def debitar(self, valor: float) -> None:
        self.__saldo = self.__saldo - (valor + (valor * self.__taxa))

    def get_taxa(self) -> float:
        return self.__taxa

    def set_taxa(self, taxa:float) -> None:
        self.__taxa = taxa