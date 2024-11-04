import conversores

def teste():
    print("25º Celsius para Fahrenheit = {}".format(conversores.celsius_para_fahrenheit(25)))
    print("100º Fahrenheit para Celsius = {}".format(conversores.fahrenheit_para_celsius(100)))
    print("100 pés para metros = {}".format(conversores.pes_para_metro(100)))
    print("100 km para milhas = {}".format(conversores.quilometro_para_milhas(100)))
    print("100 milhas para km = {}".format(conversores.milhas_para_quilometro(100)))
    print("30 dias para horas = {}".format(conversores.dia_para_horas(30)))

if __name__ == '__main__':
    teste()