def soma(a, b):
    print(a + b)

def exibe_func(f):
    print(f'Objeto da função recebido: {f}')
    print(f'Nome da função: "{f.__name__}"')

exibe_func(soma)

def meu_decorador(func):
    def meu_pacote(*args, **kwargs):
        retorno = func(*args, **kwargs)
        return retorno.upper()
    return meu_pacote

@meu_decorador
def dizer_oi(nome):
    return f'Olá, {nome}!'

print(dizer_oi("Matheus"))

def repetir_vezes(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir_vezes(3)
def dizer_oi(nome):
    print(f'Olá, {nome}!')

dizer_oi("Matheus")