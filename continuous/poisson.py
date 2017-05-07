from random import random
from math import log


def homogeneous_poisson_events(T, lam):
    """
    Para generar los eventos en las primeras T unidades de tiempo, generamos
    eventos hasta que j + 1 excede a T . El siguiente algoritmo denota I al
    número de eventos que ocurren hasta el tiempo T , S[I] indica el tiempo en
    que ocurre cada evento, 1 ≤ I ≤ n (n será el máximo valor alcanzado por I)
    """
    t = 0
    I = 0
    S = [0] * 10
    S[0] = 0
    while True:
        U = random()
        if t - log(U) / lam:
            break
        else:
            t -= log(U) / lam
        I += 1
        S[I] = t


def hom_poisson_alternative(T, lam):
    """
    Dado N (T), la distribución de los tiempos de arribo en un
    Proceso de Poisson homogéneo de razón λ es uniforme en (0, T)
    """
    pass


def non_homogeneous_poisson(lam):
    """
    Las propiedades que cumplen los procesos de poisson no homogéneos permiten
    deducir el siguiente algoritmo.
    """
    pass


def non_homogeneous_optimized(lam):
    pass
