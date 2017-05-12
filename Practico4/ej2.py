from random import random
from math import exp


def udiscreta(a, b):
    u = random()
    return int(u * (b - a + 1)) + a


def ej_2(n, k):

    # Generar k valores de U con distribución uniforme en [1, n]
    u = [udiscreta(1, n) for i in range(k)]
    # Calcular para cada uno exp(ui/k) (la función involucrada en la sumatoria)
    exps = [exp(i / n) for i in u]
    # Sumarlos, dividir por k y multiplicarlo por n
    estimation = (sum(exps) * n) / k

    real_value = sum([exp(i / n) for i in range(n)])

    print("Estimation =", estimation, "Real Value =", real_value)


# Es una buena estimación si nuestro k es igual a 100.
ej_2(10000, 100)
