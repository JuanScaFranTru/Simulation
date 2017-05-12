from collections import defaultdict
from math import log
from random import random
from discrete.discretes import poisson_optimized


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
    S[I] = 0
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
    return S


def hom_poisson_alternative(T, lam):
    """
    Dado N (T), la distribución de los tiempos de arribo en un
    Proceso de Poisson homogéneo de razón λ es uniforme en (0, T)
    """
    # Número de arribos hasta el tiempo T
    n = poisson_optimized(lam * T)
    # Dado N(T) la distribucion de los tiempos de arribo es uniforme en (0,T)
    uniforms = [random(0, T) for _ in range(n)]
    uniforms.sort()
    arrive_times = [T * U for U in uniforms]

    return arrive_times


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
        t -= - (1 / lam) * log(U)
        # Si pasaron las T unidades de tiempo, frenar.
        if t > T:
            break
        V = random()
        # Ocurre un evento?
        if V < (lamt(t) / lam):
            I += 1
            # El evento I-ésimo fué en el momento t
            S[I] = t
    return S


def non_homogeneous_optimized(lam):
    pass