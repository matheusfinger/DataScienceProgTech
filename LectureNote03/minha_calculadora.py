import calculadora as calc
# from calculadora import *

def som(a, b):
    pass

def main():
    while True:
        print("\n" + "="*82)
        operacao = input("(+) Soma | (-) Subtração  | (/) Divisão | (*) Multiplicação | (S) Sair: ")
 
        if operacao == 'S':
            break
 
        operandoA = float(input("Digite o operando A: "))
        operandoB = float(input("Digite o operando B: "))
 
        if operacao == '+':
            print(f"{operandoA} + {operandoB} = {calc.som(operandoA, operandoB)}")
        elif operacao == '-':
            print(f"{operandoA} - {operandoB} = {calc.sub(operandoA, operandoB)}")
        elif operacao == '/':
            if operandoB != 0:
                print(f"{operandoA} / {operandoB} = {calc.div(operandoA, operandoB)}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        elif operacao == '*':
            print(f"{operandoA} * {operandoB} = {calc.mut(operandoA, operandoB)}")
        else:
            print("Operação inválida, por favor tente novamente.")
 
    print("\n" + "="*82)
 
if __name__ == "__main__":
    main()
