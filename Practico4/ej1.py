from random import random

def udiscreta(a, b):
    u = random()
    return int(u * (b - a + 1)) + a


def permutations(array):
    """Produce an equiprobable permutation."""
    n = len(array)
    for j in range(n - 1, 1, -1):
        i = udiscreta(0, j)
        tmp = array[j]
        array[j] = array[i]
        array[i] = tmp
    return array

def experiment(n):
    """
    Shuffle a deck of cards numbered by 1,..., n of length n.
    After that, take cards one by one. A success is when a ith card is in the
    ith index of the deck
    """
    # Creamos el mazo con n cartas numeradas del 1 al n
    deck = [i + 1 for i in range(n)]
    # Mezclamos el mazo
    deck = permutations(deck)
    # Vemos para cada extracción de carta si es un éxito o no
    succeses = [1 for i in range(n) if deck[i] == i + 1]
    # Calculamos la cantidad de éxitos
    return sum(succeses)

def ej_1(n):

    # Realizamos el experimento para n = 100, n veces y calculamos la media
    est_succeses = sum([experiment(n) for i in range(n)])
    est_mean = est_succeses / n
    # Sólo con el fin de calcular la estimación de la varianza caculamos E[X**2]
    est_succeses2 = sum([experiment(n) ** 2 for i in range(n)])
    est_mean2 = est_succeses2 / n

    # Aqui realizamos el experimento para n = 100, n**2 veces para acercar a la
    # media a su valor real.
    succeses = sum([experiment(n) for i in range(n**2)])
    mean = succeses / n**2
    # Sólo con el fin de calcular la varianza caculamos E[X**2]
    succeses2 = sum([experiment(n) ** 2 for i in range(n**2)])
    mean2 = succeses2 / n**2

    print("Media estimada =", est_mean, "Media real =", mean)

    # Calculamos la estimación de la varianza y la varianza
    est_variance = est_mean2 - est_mean ** 2
    variance = mean2 - mean ** 2

    print("Varianza estimada =", est_variance, "Varianza real =", variance)

ej_1(100)
