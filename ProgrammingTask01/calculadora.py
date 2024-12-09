acumulador = 0

def soma(operando_a, operando_b=None):
    """
    Realiza a soma de dois números.
    """
    global acumulador
    if operando_b is None:
        operando_b = acumulador
    acumulador = operando_a + operando_b
    return acumulador

def subtracao(operando_a, operando_b=None):
    """
    Realiza a subtração de dois números.
    """
    global acumulador
    if operando_b is None:
        operando_b = acumulador
    acumulador = operando_a - operando_b
    return acumulador

def multiplicacao(operando_a, operando_b=None):
    """
    Realiza a multiplicação de dois números.
    """
    global acumulador
    if operando_b is None:
        operando_b = acumulador
    acumulador = operando_a * operando_b
    return acumulador

def divisao(operando_a, operando_b=None):
    """
    Realiza a divisão de dois números.
    """
    global acumulador
    if operando_b is None:
        operando_b = acumulador
    acumulador = operando_a / operando_b
    return acumulador