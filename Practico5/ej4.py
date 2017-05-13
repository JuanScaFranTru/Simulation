from random import random
from math import log


def exponential(lam):
    """
    Simulación de una va Exponencial con parámetro Lambda
    Dado que u ~ U(0,1) entonces (1 - u) ~ U(0,1)
    """
    u = random()
    return (- log(u)) / lam
