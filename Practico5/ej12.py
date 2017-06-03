from random import random
from collections import defaultdict
from math import log


def func_lam(t):
    return 3 + (4 / t + 1)


def non_homogeneous_poisson(T, lamt, lam):
    """
    Las propiedades que cumplen los procesos de poisson no homogéneos permiten
    deducir el siguiente algoritmo.
    :param lamt: funcion de intencidad λ(t)
    :param lam: intencidad λ tal que λ(t) <= λ
    """
    t = 0
    I = 0
    S = defaultdict(float)
    while True:
        U = random()
        t += - (1 / lam) * log(U)
        # Si pasaron las T unidades de tiempo, frenar.
        if t > T:
            break
        V = random()
        # Ocurre un evento?
        if V < (lamt(t) / lam):
            I += 1
            # El evento I-ésimo fué en el momento t
            S[I] = t
    return I, S


def experiment(T, func_lam, lam):
    total_events, events = non_homogeneous_poisson(T, func_lam, lam)
    times = list(events.items())
    print(len(times))
    print(times)


lam = 7
experiment(10, func_lam, lam)
