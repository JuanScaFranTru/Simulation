from random import random
from math import exp, log


def nroot(n):
    """
    Si se desea simular una va con distribución Fx(x) = x**n, en lugar de tomar
    una raíz n-ésima es conveniente generar n uniformes y tomar su máximo.
    """
    maxm = 0
    for i in range(n):
        U = random()
        if maxm < U:
            maxm = U
    return maxm


def exponential(lam):
    """
    Simulación de una va Exponencial con parámetro Lambda
    Dado que u ~ U(0,1) entonces (1 - u) ~ U(0,1)
    """
    U = random()
    return (- log(U)) / lam


def poisson_proc1(lam):
    n = 0
    prod = random()
    bound = exp(- lam)
    while prod < bound:
        n += 1
        prod += random()
    return  n - 1


def poisson_proc(lam, t):
    pass


def gamma(n, lam):
    """
    Una suma de n variables aleatorias exponenciales, independientes, con
    parámetro lambda es una va X ~ Gamma(m, lambda).
    """
    U = 1
    for _ in range(n):
        U *= random()
        return (- log(U)) / lam


def twoExponential(lam):
    """
    Se utiliza el siguiente teorema:

        Si X,Y ~ e(lambda), independientes, entonces
            X es condiconal a X + Y = t es uniforme en (0, t)
    """
    t = (-1 / lam) * log(random() * random())  # Valor de una Gamma(2, lambda)
    X = t * random()
    y = t - X
    return (X, Y)
