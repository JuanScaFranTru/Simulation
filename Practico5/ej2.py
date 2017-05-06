from random import random
from math import log
import matplotlib.pyplot as plt

def weibull(alpha, beta):
    """
    Dado que u ~ U(0,1) entonces (1 - u) ~ U(0,1)
    """
    u = random()
    tmp = - log(u)

    return (tmp / alpha) ** (1/beta)
