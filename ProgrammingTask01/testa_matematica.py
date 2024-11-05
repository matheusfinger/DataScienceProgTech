from matematica import *
from matematica.estatistica import media


def teste():
    print("1 + 2 = {}".format(aritmetica.soma(1, 2)))
    print("1 + 2 = {}".format(aritmetica.soma(1, 2)))
    print("Área do círculo de raio 2 = {}".format(geometria.area_circulo(2)))
    print("Área do retângulo de base 4 e altura 10 = {}".format(geometria.area_retangulo(4, 10)))
    print("Média de 5, 6, 10 e 21 = {}".format(media.media_simples([5, 6, 10, 21])))

if __name__ == '__main__':
    teste()