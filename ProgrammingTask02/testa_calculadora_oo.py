from calcudora_oo import Calculadora

def teste():
    calc = Calculadora()
    print('O resultado da adição de 13 + 14 é: {}'.format(calc.somar(13, 14)))
    print('O resultado da diminuição do acumulador por 13 é igual a: {}'.format(calc.subtrair(13)))
    print('O resultado da multiplicação do acumulador por 2 é igual a: {}'.format(calc.multiplicar(2)))
    print('O resultado da divisão do acumulador por 4 é igual a: {}'.format(calc.dividir(4)))
    

if __name__ == '__main__':
    teste()