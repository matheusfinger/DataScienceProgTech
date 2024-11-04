import calculadora as calc

def principal():
    print("1 + 2 = {}".format(calc.soma(1, 2)))
    print("1 - 2 = {}".format(calc.subtracao(1, 2)))
    print("1 * 2 = {}".format(calc.multiplicacao(1, 2)))
    print("acumulador + 2 = {}".format(calc.soma(2)))
    print("1 / 2 = {}".format(calc.divisao(1, 2)))

    print("acumulador + 2 = {}".format(calc.soma(2)))

if __name__ == "__main__":
    principal()