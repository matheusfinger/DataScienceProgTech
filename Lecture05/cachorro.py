# Se não colocar self na declaração da função,
# ela será uma função da classe, e se colocar
# ele será um método da classe.

class Cachorro:
    def __init__(self, nome:str):
        self.__nome = nome
        self.__truques = []
    def add_truque(self, truque:str) -> None:
        self.__truques.append(truque)
    def mostra_truques(self) -> list[str]:
        return self.__truques

if __name__ == '__main__':
    fido = Cachorro("fido")
    buddy = Cachorro("buddy")
    fido.add_truque("gira")
    buddy.add_truque("late")
    print(fido.mostra_truques())