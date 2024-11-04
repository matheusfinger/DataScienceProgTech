def media_simples(numeros):
    """
    Calcula a média de uma lista de números.
    """
    soma = 0
    for numero in numeros:
        soma += numero
    return soma / len(numeros)