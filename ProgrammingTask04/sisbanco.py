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
        self.__saldo -= valor

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
    
class ContaImposto(ContaAbstrata):

    def __init__(self, numero:str):
        super().__init__(numero)
        self.__taxa__ = 0.001

    def debitar(self, valor:float):
        self.__saldo = self.__saldo - (valor + (valor * self.__taxa))

    def get_taxa(self) -> float:
        return self.__taxa
    
    def set_taxa(self, taxa:float) -> None:
        self.__taxa = taxa

class Banco:
    
    def __init__(self, taxa_poupanca:float=0.001, taxa_imposto:float=0.001):
        self.__contas = []
        self.__taxa_poupanca = taxa_poupanca
        self.__taxa_imposto = taxa_imposto

    def cadastrar(self, conta: ContaAbstrata) -> None:
        self.__contas.append(conta)

    def procurar(self, numero: str) -> ContaAbstrata:
        for conta in self.__contas:
            if conta.get_numero() == numero:
                return conta
        return None
    
    def creditar(self, numero: str, valor: float) -> None:
        conta = self.procurar(numero)
        if conta is not None:
            conta.creditar(valor)

    
    def debitar(self, numero: str, valor: float) -> None:
        conta = self.procurar(numero)
        if conta is not None:
            conta.debitar(valor)

    def saldo(self, numero: str) -> float:
        conta = self.procurar(numero)
        if conta is not None:
            return conta.get_saldo()
    
    def transferir(self, origem: str, destino: str, valor: float) -> None:
        conta_origem = self.procurar(origem)
        conta_destino = self.procurar(destino)
        if conta_origem is not None and conta_destino is not None:
            conta_origem.debitar(valor)
            conta_destino.creditar(valor)

    def render_juros(self, numero:str) -> None:
        conta = self.procurar(numero)
        if isinstance(conta, ContaPoupanca):
            conta.render_juros(self.get_taxa_poupanca())
        return None
    
    def get_taxa_poupanca(self) -> float:
        return self.__taxa_poupanca
    
    def set_taxa_poupanca(self, taxa:float) -> None:
        self.__taxa_poupanca = taxa

    def get_taxa_imposto(self) -> float:
        return self.__taxa_imposto
    
    def set_taxa_imposto(self, taxa:float) -> None:
        self.__taxa_imposto = taxa

    def render_bonus(self, numero:str) -> None:
        conta = self.procurar(numero)
        if isinstance(conta, ContaEspecial):
            conta.render_bonus()
        return None