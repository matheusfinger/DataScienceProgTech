class Calculadora:

    def __init__(self):
        self.__acumulador = 0.0

    def somar(self, operando_a, operando_b=None):
        """
        Realiza a soma de dois números.
        """
        if operando_b is None:
            operando_b = operando_a
            operando_a = self.__acumulador
        self.__acumulador = operando_a + operando_b
        return self.__acumulador

    def subtrair(self, operando_a, operando_b=None):
        """
        Realiza a subtração de dois números.
        """
        if operando_b is None:
            operando_b = operando_a
            operando_a = self.__acumulador
        self.__acumulador = operando_a - operando_b
        return self.__acumulador

    def multiplicar(self, operando_a, operando_b=None):
        """
        Realiza a multiplicação de dois números.
        """
        if operando_b is None:
            operando_b = operando_a
            operando_a = self.__acumulador
        self.__acumulador = operando_a * operando_b
        return self.__acumulador

    def dividir(self, operando_a, operando_b=None):
        """
        Realiza a divisão de dois números.
        """
        if operando_b is None:
            operando_b = operando_a
            operando_a = self.__acumulador
        self.__acumulador = operando_a / operando_b
        return self.__acumulador