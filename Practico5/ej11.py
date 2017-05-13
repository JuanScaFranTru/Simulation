from collections import defaultdict
from random import random
from math import log


def homogeneous_poisson_events(T, lam):
    """
    Para generar los eventos en las primeras T unidades de tiempo, generamos
    eventos hasta que j + 1 excede a T . El siguiente algoritmo denota I al
    número de eventos que ocurren hasta el tiempo T , S[I] indica el tiempo en
    que ocurre cada evento, 1 ≤ I ≤ n (n será el máximo valor alcanzado por I)
    """
    # Es el momento 0
    t = 0
    # Ocurrieron 0 eventos
    I = 0
    S = defaultdict(float)
    while True:
        U = random()
        # Si ya pasaron las T unidades de tiempo, terminamos
        if t - log(U) / lam > T:
            break
        # Si no, avanzamos en el tiempo
        else:
            t -= log(U) / lam
        # Ocurre otro evento
        I += 1
        # En el momento t
        S[I] = t
    return I, S


def uniform_discrete(m, k):
    """Discrete Uniform distribution.
    """
    U = random()
    return int(U * (k - m + 1)) + m


def experiment(T, lam, m, k):
    total_events, events = homogeneous_poisson_events(T, lam)
    funs = 0
    times = []
    funs = sum([uniform_discrete(m, k) for _ in range(total_events)])
    times = [event[1] for event in list(events.items())]
    print("Ocurrieron eventos en los instantes:", times)
    return funs


T, lam = (1, 5)
m, k = (20, 40)
print("El total de personas que llegaron en el instante 1 es",
      experiment(T, lam, m, k))
